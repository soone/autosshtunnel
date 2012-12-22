from setuptools import setup, find_packages
import sys, os

version = '0.9'

setup(name='autosshtunnel',
      version=version,
      description="auto connect to ssh tunnel to bypass the GFW",
      long_description="""\
auto connect to ssh tunnel to bypass the GFW""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      author='soone',
      author_email='fengyue15@gmail.com',
      url='http://blog.caokee.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=['sys', 'os', 'time', 'pexpect'],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
