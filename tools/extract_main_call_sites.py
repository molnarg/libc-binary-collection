#!/usr/bin/env python

import json
import subprocess
import sys
import re
import os

def symbols_json_update(symbols_file, callback):
    other_file = open(symbols_file + '.new', 'w')
    other_file.write('{\n')
    for line in open(symbols_file, 'r').xreadlines():
        if len(line) < 3:
            continue
        [(lib, symbols)] = re.findall('^"(.*?)": (.*?),?$', line)
        symbols = json.loads(symbols)
        replacement = callback(lib, symbols)
        if replacement is None:
            other_file.write(line)
        else:
            other_file.write('"%s": %s,\n' % (lib, json.dumps(replacement)))
    if replacement is not None:
        other_file.seek(-2, 1)
        other_file.write('\n')
    other_file.write('}\n')
    os.rename(symbols_file + '.new', symbols_file)

def determine_main_call_site(libc, symbols):
    for printer in ['print_main_call_site_64', 'print_main_call_site_32']:
        printer = os.path.join(os.path.dirname(os.path.realpath(__file__)), printer)
        try:
            output = subprocess.check_output('LD_PRELOAD=%s %s' % (libc, printer), shell=True, stderr=subprocess.STDOUT)
            [(main_call_site, printf)] = re.findall('^0x([0-9a-fA-F]*) 0x([0-9a-fA-F]*)$', output)
            (main_call_site, printf) = (int(main_call_site, 16), int(printf, 16))
            print libc, main_call_site, printf
            symbols['main_call_site'] = symbols['printf'] + (main_call_site - printf)
            return symbols
        except subprocess.CalledProcessError:
            pass
        except ValueError:
            pass

symbols_json_update('symbols.json', determine_main_call_site)

