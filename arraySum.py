#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simple2DArraySum(ar):
    sum = 0
    for i in range(0, len(ar)):
        for j in range(0, len(ar[i])):
            sum = sum + ar[i][j]
    return sum

arr = np.random.randint(10, size=(1,6))
print(arr)
# print(len(arr))
print('2D==',simple2DArraySum(arr))

def simple1DArraySum(ar):
    sum = 0
    for i in range(0, len(ar)):
            sum = sum + ar[i]
    return sum

arr = np.random.randint(10, size=(6))
print(arr)
print('1D==',simple1DArraySum(arr))


# if __name__ == '__main__':
#     # fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     ar_count = int(input().strip())
#
#     ar = list(map(int, input().rstrip().split()))
#
#     result = simpleArraySum(ar)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()