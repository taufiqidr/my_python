#!/bin/python3

import math
import os
import random
import re
import sys
import datetime

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#


def dayOfProgrammer(year):
    if year <= 1917:
        if year % 4 == 0:
            dd = datetime.datetime(year, 9, 12)
            return dd.strftime("%d.%m.%Y")
        else:
            dd = datetime.datetime(year, 9, 13)
            return dd.strftime("%d.%m.%Y")
    elif year == 1918:
        dd = datetime.datetime(year, 9, 26)
        return dd.strftime("%d.%m.%Y")
    elif year > 1918:
        if year % 400 == 0:
            dd = datetime.datetime(year, 9, 12)
            return dd.strftime("%d.%m.%Y")
        elif year % 4 == 0 and year % 100 != 0:
            dd = datetime.datetime(year, 9, 12)
            return dd.strftime("%d.%m.%Y")
        else:
            dd = datetime.datetime(year, 9, 13)
            return dd.strftime("%d.%m.%Y")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
