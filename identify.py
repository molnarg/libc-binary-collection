#!/usr/bin/env python

import argparse
import ast
import json

parser = argparse.ArgumentParser(description='Identify the libc version and find unknown symbol addresses based on known symbol addresses.')
parser.add_argument('symbol', nargs='+', metavar='symbol=address|?')
args = parser.parse_args()

known_symbols = {}
query_symbols = []
for symbol in args.symbol:
  if '=' not in symbol:
    symbol += '=?'
  [name, address] = symbol.split('=')
  if address == '?':
    query_symbols.append(name)
  else:
    known_symbols[name] = ast.literal_eval(address)

alignment = 4096

db = json.loads(open('symbols.json').read())
for libc in db:
  libc_symbols = db[libc]
  for key in known_symbols:
    # Checks on each known symbol (presence, alignment)
    if ((key not in libc_symbols) or
        (known_symbols[key] % alignment != libc_symbols[key] % alignment) or
	(known_symbols[key] < libc_symbols[key])):
      break
  else:
    # Checks on symbol-pairs (address differences must match)
    known_symbol_names = known_symbols.keys()
    first = known_symbol_names[0]
    if len(known_symbol_names) > 1:
      for other in known_symbol_names[1:]:
        if known_symbols[first] - known_symbols[other] != libc_symbols[first] - libc_symbols[other]:
	  continue

    # Printing results
    if len(query_symbols) == 0:
      print libc
    else:
      offset = known_symbols[first] - libc_symbols[first]
      print libc,
      for query_name in query_symbols:
        print '%s=0x%x' % (query_name, libc_symbols[query_name] + offset),
      print

