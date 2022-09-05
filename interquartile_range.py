#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#


def medians(half):
    n = len(half)
    mid = 0
    if n % 2 == 0:
        mid = (half[int(n/2)] + half[int((n/2)-1)])/2
    else:
        mid = half[int(n/2-0.5)]

    return int(mid)


def interQuartile(values, freqs):
    interq = 0
    arr_str = []
    arrst = []
    arr = []
    for i in range(len(values)):
        arr_str.append((str(values[i])+" ") * freqs[i])
        arrst.append(arr_str[i].split())

    for i in range(len(arrst)):
        for j in arrst[i]:
            arr.append(int(j))

    arr.sort()
    n = len(arr)
    quartz = [0, 0, 0]
    if n % 2 == 0:
        mid = int(len(arr)/2)
        upper = arr[mid:]
        lower = arr[:mid]
    else:
        mid = int(len(arr)/2 + 0.5)
        upper = arr[mid:]
        lower = arr[:mid-1]

    quartz[0] = medians(lower)
    quartz[1] = medians(arr)
    quartz[2] = medians(upper)
    interq = quartz[2] - quartz[0]

    print(round(float(interq), 1))


if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
