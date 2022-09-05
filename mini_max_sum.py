#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    mini=0
    maxi = 0
    summed = []
    sums = sum(arr)
    # Write your code here
    for i in range(len(arr)):
        
        summed.append(sums - arr[i])
    
    mini = min(summed)
    maxi = max(summed)

    print(str(mini) + " " + str(maxi))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
