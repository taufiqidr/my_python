#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
import operator
#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def equalizeArray(arr):
    maxx = (Counter(arr))
    sorted_d = dict(
        sorted(maxx.items(), key=operator.itemgetter(1), reverse=True))
    sorted_keys = list(sorted_d.keys())
    sorted_values = list(sorted_d.values())
    sorted_values.pop((sorted_values.index(max(sorted_values))))
    return(sum(sorted_values))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
