#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#
#0 3 4 2

def kangaroo(x1, v1, x2, v2):
    jump = 1
    if x2 > x1 and v2 > v1:
        return "NO"
    
    xx1 =x1+v1
    xx2 =x2+v2
    
    while jump < 10000:
        if( xx1==xx2 ):
            return "YES"
            break
        
        if jump > 5000:
            if xx1 > xx2:
                return "NO"
                break
            else:
                return "NO"
                break
        
        xx1 = xx1 + v1
        xx2 = xx2 + v2
        jump = jump+1
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
