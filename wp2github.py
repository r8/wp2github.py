#!/usr/bin/env python
"""
Copyright (c) 2013, Sergey Storchay.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
import argparse, string, re, sys
from collections import OrderedDict

def parse_arguments():
    p = argparse.ArgumentParser(
        description='Convert WordPress plugin readme file '
        + 'to GitHub Flavored Markdown',
        version='wp2github.py 1.0')

    p.add_argument('--source', '-s', default='readme.txt',
                    help='Source file path (default: readme.txt)')
    p.add_argument('--target', '-t', default='README.md',
                    help='Destination file path (default: README.md)')

    return p.parse_args()

def convert(source, target):
    try:
        input_file = open(source, 'r')
    except Exception, e:
        print "Error opening source file: %s" % source
        sys.exit(1)

    name, data = split_sections(input_file.readlines())
    input_file.close()

    output = format_header(name, data['main'])

    for name in data.keys():
        output += format_section(name, data[name])

    try:
        output_file = open(target, 'w')
    except Exception, e:
        print "Error opening target file: %s" % target
        sys.exit(1)

    output_file.write(output)
    output_file.close()

def split_sections(data):
    name = data.pop(0).strip("= \r\n")

    output = OrderedDict()
    section_name = 'main'
    section_body = ''

    for line in data:
        section_match = re.match('^==[^=]*?==', line)
        if section_match:
            output[section_name] = section_body.rstrip(" \r\n")
            section_body = ''
            section_name = line.strip("= \r\n").lower()
        else:
            section_body += line.replace("\r\n", "\n").replace("\r", "\n")

    if section_body:
        output[section_name] = section_body

    return name, output

def format_header(name, data):
    output = "# %s\n\n" % name

    list_item = True
    for line in data.split("\n"):
        if not line:
            list_item = False

        if list_item:
            output += "* "
        output += "%s\n" % line

    return output

def format_section(name, data):
    if name in ['main', 'screenshots']:
        return ''

    output = "\n## %s\n" % string.capwords(name)

    for line in data.split("\n"):
        output += "%s\n" % format_line(line)

    return output

def format_line(line):
    line = re.sub(r'^=([^=]*?)=', r'###\1', line)
    return line

def main():
    arguments = parse_arguments()
    if not arguments: sys.exit(2)

    convert(arguments.source, arguments.target)

if __name__ == '__main__':
    main()
