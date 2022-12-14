#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib



"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++

  urls = set()   ##Using set to eliminate the duplicates
  f = open(filename)
  # file = f.read()
  # print(file)
  for lines in f:
    # print(lines)
    match_urls = re.search(r'GET (\S+)', lines)  ##\S matches non-space char
    res_match_urls = match_urls.group(1)
    urls.add("http:/" + res_match_urls)  ##using .add to add the element and set will eliminate the duplicates.

  ascending_order = sorted(urls)   ##sorting it into the ascending order


  slice_result = ascending_order[8:28]
  # print(slice_result)
  return slice_result



  # print(ascending_order)
  # return ascending_order



def download_images(img_urls, dest_dir):

  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++

  if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

  ##Creating a new file in order to store the html lines

  new_file = file(os.path.join(dest_dir, 'index.html'), 'w')
  new_file.write('<html>\n<body>\n')

  i = 0
  ##printing the urls in order to have img numbers besides it
  for url in img_urls:
    local_name = 'img%d' % i
    print('Retrieving', url)

    ##Using package urllib to download the image and then merge the directory with image numbers
    var = urllib.urlretrieve(url, os.path.join(dest_dir, local_name))
    print(var)
    ##Writing the file img src according to the qustion
    new_file.write('<img src= %s' % local_name)
    i = i+1

    ##End part of html and closing the file
    new_file.write('\n</body></html>')
    new_file.close()


  print(new_file)

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)



if __name__ == '__main__':
  main()
