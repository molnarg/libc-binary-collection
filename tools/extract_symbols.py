#!/usr/bin/env python

import re
import sys
import json
import os.path
import subprocess
from distutils.spawn import find_executable

so_file = sys.argv[1]
csv_file = sys.argv[2]

def symbols(file):
  try:
    output = subprocess.check_output([find_executable('gnm') or find_executable('nm'), '-D', file], stderr=subprocess.STDOUT)
  except subprocess.CalledProcessError:
    output = subprocess.check_output([find_executable('gnm') or find_executable('nm'), '-D', '--target=elf32-i386', file])
  symbols = {}
  for line in output.split('\n'):
    fields = re.findall('^([0-9a-fA-F]+) (.) (.+)$', line)
    if len(fields) != 1:
      continue
    fields = fields[0]
    symbols[fields[2]] = int(fields[0], 16)
  return symbols

def append_symbols_to_json(so_file, json_file):
  if os.path.exists(json_file):
    file = open(json_file, 'r+')
    file.seek(-2, 2)
  else:
    file = open(json_file, 'w')
    file.write('{\n')

  file.write('"%s": %s\n}\n' % (so_file, json.dumps(symbols(so_file))))

if not os.path.isfile(so_file):
  print 'File not found: %s' % so_file
  sys.exit()

append_symbols_to_json(so_file, csv_file)

