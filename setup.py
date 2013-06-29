#!/usr/bin/env python

from setuptools import setup
from wp2github import _version

# Get the requirements from the pip requirements file
requirements = []

with open("requirements.txt") as f:
    for l in f:
        l = l.strip()
        if l:
            requirements.append(l)

setup(name="wp2github",
      version=_version.__version__,
      description="Convert WordPress plugin readme file to GitHub Flavored Markdown",
      long_description=open("README.rst").read(),
      author="Sergey Storchay",
      author_email="r8@r8.com.ua",
      url="https://github.com/r8/wp2github.py",
      license="MIT",
      packages=["wp2github"],
      entry_points={"console_scripts": ["wp2github = wp2github.wp2github:main"]},
      install_requires=requirements
)