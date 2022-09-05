#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#


def viralAdvertising(n):
    init_share = [5]
    init_liked = []

    for i in range(n-1):
        people = math.floor(init_share[i]/2)*3
        init_share.append(people)
    for like in init_share:
        init_liked.append(math.floor(like/2))

    return sum(init_liked)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
