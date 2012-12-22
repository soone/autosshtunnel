autosshtunnel
=============

auto connect to ssh tunnel to bypass the GFW

Required
-------------
* pexpect

Install
-------------
1. python setup.py build
2. python setup.py install
3. open the autosshtunnel/autosshtunnel.py file and edit the HOST,USER,PASS,PORT parameter to yourself's value

Usage
-------------
python autosshtunnel.py

to kill the autosshtunnel process use the command below:
`ps aux|grep autosshtunnel|grep -v "grep"|awk '{print $2}'|xargs kill {}\;`

How to use ssh tunnel on firefox and chrome
-------------
see [here](http://www.luochunhui.com/%E4%BD%BF%E7%94%A8ssh%E9%9A%A7%E9%81%93%E7%BF%BB%E5%A2%99/)
