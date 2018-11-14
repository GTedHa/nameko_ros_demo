#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['ros_nameko_node'],
    scripts=[
        'scripts/run_node.py',
    ],
)

setup(**d)