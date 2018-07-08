#!/usr/bin/env python3

from setuptools import setup

setup(
    name="liedetector",
    version="1.0",
    description="Your terminal knows if you're lying...",
    long_description=open("README.md").read(),
    license="MIT",
    packages=["libliedetector"],
    scripts=["liedetector"],
    package_data={"libliedetector": ["data/*"]},
)
