import sys
import os
import time
import pexpect
HOST = "192.168.1.201"  # Your vps host
USER = "soone"  # ssh tunnel user
PASS = "123456"  # ssh tunnel user password
PORT = 8000  # local port


def daemonize(stdout="/dev/null", stderr=None, stdin="/dev/null", pidfile=None, startmsg="started with pid %s"):

    #Do first fork.
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError, e:
        sys.stderr.write("fork #1 failed: %d (%s)" % (e.errno, e.stderror))
        sys.exit(1)

    #Decouple from parent environment
    os.chdir('/')
    os.umask(0)
    os.setsid()

    #Do second fork
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError, e:
        sys.stderr.write("fork #2 failed: %d (%s)\n" % (e.errno, e.strerror))
        sys.exit(1)

    if not stderr:
        stderr = stdout
        si = file(stdin, "r")
        # note that these files must have ABSOLUTE paths
        so = file(stdout, "a+")
        se = file(stderr, "a+", 0)
        pid = str(os.getpid())
        sys.stderr.write("%s\n" % startmsg % pid)
        sys.stderr.flush()
        if pidfile:
            file(pidfile, "w+").write("%s\n" % pid).flush()

        # Redirect standard file descriptors.
        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(so.fileno(), sys.stdout.fileno())
        os.dup2(se.fileno(), sys.stderr.fileno())


def sshTunnel():
    child = pexpect.spawn("ssh -C -N -f -D %d %s@%s" % (PORT, USER, HOST))
    i = child.expect([pexpect.TIMEOUT, 'Are you sure you want to continue connecting', 'password: '])
    if i == 0:
        sys.stderr.write("unknown error\n")
        sys.stderr.flush()
        return
    elif i == 1:
        child.sendline('yes')

    child.sendline(PASS)
    child.expect(pexpect.EOF)
    sys.stdout.write("OK\n")
    sys.stdout.flush()
    return

if __name__ == "__main__":
    daemonize()
    while 1:
        tunnelProc = os.popen("ps aux|grep 'ssh -C'|grep -v 'grep'|grep -v 'ssh-agent'|wc -l").read().strip()
        if tunnelProc == "0":
            sshTunnel()

        time.sleep(10)
