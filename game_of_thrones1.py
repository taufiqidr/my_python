#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def gameOfThrones(string):

    NO_OF_CHARS = 256
    # Create a count array and initialize all
    # values as 0
    count = [0 for i in range(NO_OF_CHARS)]

    # For each character in input strings,
    # increment count in the corresponding
    # count array
    for i in string:
        count[ord(i)] += 1

    # Count odd occurring characters
    odd = 0
    for i in range(NO_OF_CHARS):
        if (count[i] & 1):
            odd += 1

        if (odd > 1):
            return "NO"

    # Return true if odd count is 0 or 1,
    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
