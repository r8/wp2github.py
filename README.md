wp2github.py
============

Command-line tool that converts WordPress-style Readme file to GitHub Markdown Readme.

Inspired by https://github.com/benbalter/WP-Readme-to-Github-Markdown

Requirements
------------

Python 2.7

Installation
------------

    python setup.py install

This will create a `wp2github` script in /usr/local/bin (linux) or c:\Python2.7\Scripts (windows)

Usage
-----

See: `wp2github -h`

For example:

    wp2github --source SOURCE.txt --target TARGET.md

Versioning
----------

This project implements the Semantic Versioning guidelines.

Releases will be numbered with the following format:

`<major>.<minor>.<patch>`

And constructed with the following guidelines:

* Breaking backward compatibility bumps the major (and resets the minor and patch)
* New additions without breaking backward compatibility bumps the minor (and resets the patch)
* Bug fixes and misc changes bumps the patch

For more information on SemVer, please visit [http://semver.org](http://semver.org).

License
-------

Copyright (c) 2013 Sergey Storchay, [http://r8.com.ua](http://r8.com.ua)

Licensed under MIT: [https://raw.github.com/r8/wp2github.py/master/LICENSE](https://raw.github.com/r8/wp2github.py/master/LICENSE)

