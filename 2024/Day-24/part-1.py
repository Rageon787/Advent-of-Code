import sys

filename = sys.argv[1]

with open(filename) as f:
    raw_input = f.read()
