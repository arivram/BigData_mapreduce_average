"""reducer.py"""

from operator import itemgetter
import sys

average = 0
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

average = (total_Sum/total_count)
print('average = ' + str(average))
