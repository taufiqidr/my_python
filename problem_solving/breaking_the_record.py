#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#


def breakingRecords(scores):
    mint = scores[0]
    maxt = scores[0]
    timed = [0, 0]
    for i in range(len(scores)):
        if i > 0:
            if scores[i] > maxt:
                maxt = scores[i]
                timed[0] += 1
            elif scores[i] < mint:
                mint = scores[i]
                timed[1] += 1

    return timed


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
