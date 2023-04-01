#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

sum = 0
count = 0
total_Sum = 0
total_count = 0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    sum, count = line.split('\t', 1)

    try:
        sum = int(sum)
        count = int(count)
    except ValueError:
        continue

    total_Sum += sum
    total_count += count

# calculate the average
if total_count > 0:
    average = total_Sum / total_count
else:
    average = 0

print('average = ' + str(average))
