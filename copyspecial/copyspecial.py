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
def get_special_files(dirName):
  result = []
  fileNames = os.listdir(dirName)
  for fileName in fileNames:
    matched_file_names = re.search(r'__(\w+)__',fileName)
    if matched_file_names:
      absFileName = os.path.abspath(fileName)
      result.append(absFileName)
  return result
def copy_special_files(srcFilePaths,destDir):
  if not os.path.exists(destDir):
    os.makedirs(destDir)
  for filePath in srcFilePaths:
    fileName = os.path.basename(filePath)
    shutil.copy(filePath,os.path.join(destDir,fileName))

def zip_to(paths,zipPath):
  cmd = 'zip -j '+zipPath+' '+' '.join(paths)
  #print 'command to be exec='+cmd
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write(output)
    sys.exit(1)
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
  filtered_files = []
  for dirName in args:
    filtered_files.extend(get_special_files(dirName))

  if todir != '':
    copy_special_files(filtered_files,todir)

  if tozip !='':
    zip_to(filtered_files,tozip)
  
if __name__ == "__main__":
  main()
