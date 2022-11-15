#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them


# def to_dir(target_dir, source_dirs):
#     # print("source_dirs", source_dirs)
#     for source_dir in os.listdir(source_dirs):
#         print("source_dir", source_dir)
#     # source_dir = source_dirs[0]
#     # source_dir_files = os.listdir(source_dir)
#     # print("source_dir_files", source_dir_files)

def get_abs_path(source_dirs):
    files = []
    for source_dir in source_dirs:
        source_dir_files = os.listdir(source_dir)
        x = os.path.abspath(os.path.join(source_dirs, source_dir))
        print("x", x)
        files.append(x)
    # current: [['x.txt', 'y.txt'], ['a.txt'], ['m.txt']]
    # ideal: ['x.txt', 'y.txt', 'a.txt', 'm.txt']
    print(files)
    return files


def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.

    # terminal input: python copyspecial.py --todir myfolder --tozip myzipfile foo bar baz
    # sys.argv = ['copyspecial.py', '--todir', 'myfolder', '--tozip', 'myzipfile', 'foo', 'bar', 'baz']

    # ['--todir', 'myfolder', '--tozip', 'myzipfile', 'foo', 'bar', 'baz']
    args = sys.argv[1:]
    if not args:
        print "usage: [--todir dir][--tozip zipfile] dir [dir ...]"
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    # ['--todir', 'myfolder', '--tozip', 'myzipfile', 'foo', 'bar', 'baz']
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    # ['--tozip', 'myzipfile', 'foo', 'bar', 'baz']
    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    # ['foo', 'bar', 'baz']
    if len(args) == 0:
        print "error: must specify one or more dirs"
        sys.exit(1)

    get_abs_path(args)

    # if todir:
    #     to_dir(todir, args)

    # +++your code here+++
    # Call your functions


if __name__ == "__main__":
    main()
