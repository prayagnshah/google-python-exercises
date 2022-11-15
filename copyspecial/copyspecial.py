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

#Milestone No.1
def get_special_paths(dir):
  files = []  ##we will store pathname in the empty list

  ##iterating the filename which we mention in the directory

  for path in os.listdir(dir):
    # print(path)

#output: a.txt, b.txt, copyspecial.pysolution, test.py, xyz__hello__.txty.txt, zz__something__.jpg
#   #   if re.match(r'.(\w+)', path):
    files.append(os.path.abspath(os.path.join(dir, path)))
  print(files)

##output:  ['D:\\github\\google-python-exercises\\copyspecial\\a.txt', 'D:\\github\\google-python-exercises\\copyspecial\\b.txt',
# 'D:\\github\\google-python-exercises\\copyspecial\\copyspecial.py', 'D:\\github\\google-python-exercises\\copyspecial\\solution',
# 'D:\\github\\google-python-exercises\\copyspecial\\test.py', 'D:\\github\\google-python-exercises\\copyspecial\\xyz__hello__.txt',
# 'D:\\github\\google-python-exercises\\copyspecial\\y.txt', 'D:\\github\\google-python-exercises\\copyspecial\\zz__something__.jpg']

#   return


def copy_to(paths, dir):

  ##Will check if the path exists or not. If not, then it will create new directory
  if not os.path.exists(dir):
    os.makedirs(dir)

  ##Copying the files from paths to dir directory using the fucntion shutil
  for path in paths:
    shutil.copy(path, os.path.join(dir))
    print(path)



  # file = []

  # ##Retrieving the list of files in given directory
  # for path in os.listdir(dir):
  #   os.path.isfile(os.path.join(dir, path))   ##joining the files in that directory
  #   shutil.copy(os.path.join(dir, path), paths)  ##copying those files into the target destination paths
  #   print(path)




  return

def zip_to(paths, zippath):

  # var = get_special_paths(zippath)
  # print(var)
  # zip_file = 'zip -j' + zippath + ' ' + ' '.join(paths)
  # (status, output) = commands.getstatusoutput(zip_file)

  # if status:
  #   sys.stderr.write(output)
  #   sys.exit(1)

  # print("I am going to do: " + zip_file)
  return



def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)


  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]


  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)





  # +++your code here+++
  # Call your functions
  paths = []
  for dir in args:
    var = get_special_paths(dir)  ##storing all the types of values in empty variable paths



  # if todir:
  #   copy_to(paths, todir)
  # elif tozip:
  #   zip_to(paths,tozip)
  # else:
  #   print(paths)



  # # print(file)





if __name__ == "__main__":
  main()
