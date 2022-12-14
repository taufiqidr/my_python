#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMinCost' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY crew_id
#  2. INTEGER_ARRAY job_id
#

def getMinCost(crew_id, job_id):

    cost = 0
    crew_id.sort()
    job_id.sort()
    
    len1 = len(crew_id)
    len2 = len(job_id)
    
    if len1 == len2:
        for i in range(len1):
            if job_id[i]>=crew_id[i]:
                cost = cost+(job_id[i]-crew_id[i])
            elif job_id[i]<crew_id[i]:
                cost = cost+(crew_id[i]-job_id[i])
    return cost            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crew_id_count = int(input().strip())

    crew_id = []

    for _ in range(crew_id_count):
        crew_id_item = int(input().strip())
        crew_id.append(crew_id_item)

    job_id_count = int(input().strip())

    job_id = []

    for _ in range(job_id_count):
        job_id_item = int(input().strip())
        job_id.append(job_id_item)

    result = getMinCost(crew_id, job_id)

    fptr.write(str(result) + '\n')

    fptr.close()
