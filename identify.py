#!/usr/bin/env python

import argparse
import ast
import json

alignment = 4096
db = json.loads(open('symbols.json').read())

def identify_libc(**kwargs):
    global db
    query_symbols = filter(lambda k: kwargs[k] is None, kwargs.keys())
    known_symbols = {key: kwargs[key] for key in kwargs if key not in query_symbols}
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
                ok = True
                for other in known_symbol_names[1:]:
                    if known_symbols[first] - known_symbols[other] != libc_symbols[first] - libc_symbols[other]:
                        ok = False
                        break
                if not ok:
                    continue
            # Yielding results
            offset = known_symbols[first] - libc_symbols[first]
            found_symbols = {symbol: libc_symbols[symbol] + offset for symbol in query_symbols}
            yield libc, found_symbols

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Identify the libc version and find unknown symbol addresses based on known symbol addresses.')
    parser.add_argument('symbol', nargs='+', metavar='symbol=address|?')
    args = parser.parse_args()

    symbols = {}
    for symbol in args.symbol:
        if '=' not in symbol:
            symbol += '=?'
        [name, address] = symbol.split('=')
        symbols[name] = None if (address == '?') else ast.literal_eval(address)

    for libc, identified_symbols in identify_libc(**symbols):
        for symbol in identified_symbols:
            print '%s=0x%016x' % (symbol, identified_symbols[symbol]),
        print libc

