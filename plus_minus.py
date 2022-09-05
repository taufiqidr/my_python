#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    length = len(arr)
    neg = 0
    pos = 0
    zero = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            pos = pos + 1
            
        elif arr[i] < 0:
            neg = neg + 1

        else:
            zero = zero + 1

    positif =pos/length
    negatif = neg/length
    nol = zero/length
    print ("%.5f" % positif)
    print ("%.5f" % negatif)
    print ("%.5f" % nol)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
