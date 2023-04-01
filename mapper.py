#!/usr/bin/env python
"""mapper.py"""

import sys

sum = 0
count = 0

# input comes from STDIN (standard input)
for line in sys.stdin:

    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    numbers = line.split()
    # increase counters
    for number in numbers:
        try:
         number = int(number)
        except ValueError:
         continue
        count += 1
        sum += number

print('%s\t%s' % (sum, count))
