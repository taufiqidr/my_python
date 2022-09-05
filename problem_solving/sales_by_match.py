#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
import operator
#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#


def sockMerchant(n, arr):
    # 28
    maxx = (Counter(arr))
    maxx2 = (Counter(arr))
    err = 0

    for key in maxx:
        if maxx[key] <= 1:
            maxx2.pop(key)
        if maxx[key] % 2 != 0 and maxx[key] > 2:
            maxx2[key] -= 1

    pairs = int(sum(maxx2.values())/2)
    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
