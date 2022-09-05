#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def cutTheSticks(arr):
    target = [0]*len(arr)
    temp = []
    store = []
    cut = 0
    while arr != target:
        cut = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                temp.append(arr[i])

        low = min(temp)
        for i in range(len(arr)):

            if arr[i]-low >= 0:
                cut += 1

            if arr[i] != 0:
                arr[i] = arr[i]-low

        temp = []
        store.append(cut)

    return store


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
