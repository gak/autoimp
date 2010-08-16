#!/usr/bin/env python

from distutils.core import setup

import autoimp

setup(name='autoimp',
      version=autoimp.__version__,
      description='Import all modules, load them lazily at first use.',
      author='Connelly Barnes',
      url='http://www.connellybarnes.com/code/autoimp/',
      packages=['autoimp'],
     )
