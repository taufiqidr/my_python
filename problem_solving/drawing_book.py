#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#


def pageCount(n, p):
    book = [[1]]
    book2 = [[1]]

    front_turn = 0
    back_turn = 0

    if p == 1:
        return 0

    for i in range(2, n):
        book.append([i, i+1])

    for i in range(0, len(book)):
        if i > 0:
            if i % 2 != 0:
                book2.append(book[i])
    if n % 2 == 0:
        book2.append([n])
    for i in range(len(book2)):
        if p in book2[i]:
            front_turn = i
            break

    for i in range(len(book2)-1, 0, -1):
        if p in book2[i]:
            break
        back_turn += 1

    return min(back_turn, front_turn)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
