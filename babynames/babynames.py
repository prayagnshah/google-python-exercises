#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re


"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  year = []
  f = open(filename, 'rU')
  words = f.read()   ##reading the whole html file
  # print(words)

  ##using the \s for the whitespace and \d to find the digits
  year_match = re.search(r'Popularity\sin\s(\d\d\d\d)', words)  ##getting the year from the html file.

##using .group function to bring the 1st substring of the html file
  res_year = year_match.group(1)
  year.append(res_year)
  print(year)

## using \d+ will bring one or more occurences after the string or number
## for eg, if for 1990 and if \d used then it will just print empty string

  name_rank = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', words)

  # print(name_rank)

  ## Getting the names data into dict
  names_rank = {}

  for rank,boy_name,girl_name in name_rank:

##Adding boy name and girl name in empty dictionary names_rank
    names_rank[boy_name] = rank
    names_rank[girl_name] = rank

  print(names_rank)





def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]





  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  for filename in args:
    names = extract_names(filename)
    # res = names_data(filename)
    # text = " ".join(names)
    # return text



  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file



  # for filename in args:
  #   # names = extract_names(filename)
  #   print(filename)
  #   names = extract_names(f)
  #   lines = '\n'.join(names)

  #   if summary:
  #     f = open(f, 'w')
  #     f.write(lines)
  #     f.close()

  #   else:
  #     print(lines)


if __name__ == '__main__':
  main()
