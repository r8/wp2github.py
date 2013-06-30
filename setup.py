#!/usr/bin/env python

from setuptools import setup
from wp2github import config

# Get the requirements from the pip requirements file
requirements = []

with open('requirements.txt') as f:
    for l in f:
        l = l.strip()
        if l:
            requirements.append(l)

setup(
    name=config.__title__,
    version=config.__version__,
    description=config.__description__,
    long_description=open('README.rst').read() + '\n\n' + open('CHANGELOG.rst').read(),
    author=config.__author__,
    author_email=config.__author_email__,
    url=config._url_,
    license=open('LICENSE.txt').read(),
    packages=['wp2github'],
    entry_points={'console_scripts': ['wp2github = wp2github.wp2github:main']},
    install_requires=requirements,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Markup',
    ),
)
