#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#


def utopianTree(n):
    if n == 0:
        initial = 1
        return initial
    else:
        initial = 1
        for i in range(n):
            if i % 2 == 0 and i != 0:
                initial *= 2
            else:
                initial += 1
        return initial


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
