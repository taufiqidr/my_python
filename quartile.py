#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def medians(half):
    n = len(half)
    mid = 0
    if n%2 == 0:
        mid = (half[int(n/2)] + half[int((n/2)-1)])/2
    else:
        mid = half[int(n/2-0.5)]
    
    return int(mid)

def quartiles(arr):
    arr.sort()
    n = len(arr)
    quartz = [0,0,0]
    if n%2 == 0:
        mid=int(len(arr)/2)
        upper = arr[mid:]
        lower = arr[:mid]
    else:
        mid=int(len(arr)/2 + 0.5) 
        upper = arr[mid:]
        lower = arr[:mid-1]

    quartz[0] = medians(lower)
    quartz[1] = medians(arr)
    quartz[2] = medians(upper)
    return quartz

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
