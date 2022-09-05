#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import date
import datetime


#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#

def libraryFine(d1, m1, y1, d2, m2, y2):

    date1 = datetime.date(y1, m1, d1)
    date2 = datetime.date(y2, m2, d2)
    delta_days = (date1-date2).days

    if delta_days <= 0:
        return 0
    elif delta_days > 0 and m1 == m2 and y1 == y2:
        return delta_days*15
    elif delta_days > 0 and m1 > m2 and y1 == y2:
        return abs(m1-m2)*500
    elif delta_days > 0 and y1 >= y2:
        return abs(y1-y2)*10000


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    d1 = int(first_multiple_input[0])

    m1 = int(first_multiple_input[1])

    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()

    d2 = int(second_multiple_input[0])

    m2 = int(second_multiple_input[1])

    y2 = int(second_multiple_input[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
