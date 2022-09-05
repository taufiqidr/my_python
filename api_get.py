#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getAuthorHistory' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING author as parameter.
#
# Base urls:
#   https://jsonmock.hackerrank.com/api/article_users?username=
#   https://jsonmock.hackerrank.com/api/articles?author=
#
import json
import requests
def getAuthorHistory(author):
    history = []
    url1= "https://jsonmock.hackerrank.com/api/article_users?username={0}".format(author)
    url2 = "https://jsonmock.hackerrank.com/api/articles?author={0}".format(author)
    
    response1 = requests.get(url1)
    response2 = requests.get(url2)
    
    result1 = response1.json()
    result2 = response2.json()
    
    totalpage1= result1['total']
    totalpage2= result2['total']
    
    for i in range (totalpage1):
        if result1['data'][i]['about'] == 'null' or result1['data'][i]['about'] == '' :
            continue
        else:
            history.append(result1['data'][i]['about'])
        
    for i in range (totalpage2):
        if result2['data'][i]['title'] == 'null' or result2['data'][i]['title'] == '':
            history.append(result2['data'][i]['story_title'])
        elif result2['data'][i]['title'] == 'null' and result2['data'][i]['story_title'] == 'null' and result2['data'][i]['title'] == '' and result2['data'][i]['story_title'] == '':
            continue
        else:
            history.append(result2['data'][i]['title'])
            
    return history
    
    

    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    author = input()

    result = getAuthorHistory(author)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
