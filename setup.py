#!/usr/bin/env python

from platform import python_version_tuple

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if python_version_tuple()[0] < "3":
    raise ValueError("Error python version. Need python3 and more")

setup(
    name="dump",
    version="0.8.10",
    description="Dump function to YAML/JSON",
    author="HiKami",
    url="https://github.com/HiKami172/ISP-lab2",
    setup_requires=["wheel"],
    install_requires=["pyyaml", "wheel"],
    packages=["lib/utils", "lib/json", "lib/factory", "app"],
    entry_points={"console_scripts": "dump=app.command_line:main"},
)
