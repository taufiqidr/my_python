#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
import operator
#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def migratoryBirds(arr):
    maxx = (Counter(arr))
    sorted_d = dict(
        sorted(maxx.items(), key=operator.itemgetter(1), reverse=True))
    sorted_keys = list(sorted_d.keys())
    sorted_values = list(sorted_d.values())
    if sorted_keys[0] > sorted_keys[1] and sorted_values[1] >= sorted_values[0]:
        return sorted_keys[1]
    else:
        return sorted_keys[0]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
