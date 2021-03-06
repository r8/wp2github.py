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
import string
import sys
import re
import argparse
from collections import OrderedDict
import config


class Wp2github:
    arguments = []

    def __init__(self):
        self.arguments = self.parse_arguments()
        if not self.arguments:
            sys.exit(2)

    def parse_arguments(self):
        p = argparse.ArgumentParser(
            description=config.__description__,
            version='%s %s' % (config.__title__, config.__version__))

        p.add_argument('--source', '-s', default='readme.txt',
                       help='Source file path (default: readme.txt)')
        p.add_argument('--target', '-t', default='README.md',
                       help='Destination file path (default: README.md)')
        p.add_argument('--image-extension', '-e', default='png',
                       help='Extension of screenshot files (default: png)')

        return p.parse_args()

    def convert(self, source, target):
        try:
            input_file = open(source, 'r')
        except IOError:
            print "Error opening source file: %s" % source
            sys.exit(1)

        name, data = self.split_sections(input_file.readlines())
        input_file.close()

        output = self.format_header(name, data['main'])

        for name in data.keys():
            output += self.format_section(name, data[name])

        try:
            output_file = open(target, 'w')
        except IOError:
            print "Error opening target file: %s" % target
            sys.exit(1)

        output_file.write(output)
        output_file.close()

    def split_sections(self, data):
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

    def format_header(self, name, data):
        output = "# %s\n\n" % name

        list_item = True
        for line in data.split("\n"):
            if not line.strip():
                list_item = False

            if list_item:
                output += "* "
            output += "%s\n" % line

        return output

    def format_section(self, name, data):
        if name == 'main':
            return ''

        output = "\n## %s\n" % string.capwords(name)

        if name == 'screenshots':
            return output + self.format_screenshots(data)

        for line in data.split("\n"):
            output += "%s\n" % self.format_line(line)

        return output

    def format_line(self, line):
        line = re.sub(r'^=([^=]*?)=', r'###\1', line)
        return line

    def format_screenshots(self, data):
        output = ''
        i = 0

        for line in data.split("\n"):
            if not line.strip():
                output += "%s\n" % line
            else:
                i += 1
                text = re.sub(r'^[0-9]+\.\s+(.*?)', r'\1', line)
                link = self.format_screenshot_link(i)
                output += "![%s](%s \"%s\")     \n_%s_\n\n" % (text, link, text, text)

        return output

    def format_screenshot_link(self, i):
        link = "screenshot-%i.%s" % (i, self.arguments.image_extension)
        return link

    def run(self):
        self.convert(self.arguments.source, self.arguments.target)

def main():
    wp2github = Wp2github()
    wp2github.run()

if __name__ == '__main__':
    main()
