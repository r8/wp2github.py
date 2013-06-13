#!/usr/bin/env python

from setuptools import setup

setup(name="wp2github",
            version="1.0.1",
            description="Convert WordPress plugin readme file to GitHub Flavored Markdown",
            long_description=open("README.md").read(),
            author="Sergey Storchay",
            author_email="r8@r8.com.ua",
            url="https://github.com/r8/wp2github.py",
            license="MIT",
            packages=["wp2github"],
            entry_points = { "console_scripts" : [ "wp2github = wp2github.wp2github:main"]},
           )