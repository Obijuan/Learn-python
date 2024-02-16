#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
print(f"* Argumento lines: {args.lines}")  
print(f"* Argumento filenames: {args.filenames}")
