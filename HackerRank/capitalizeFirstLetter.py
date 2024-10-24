#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):

    words = re.findall(r'(\S+\s*)', s)
    return_string =''
    for word in words:
        return_string += word[0].upper() + word[1:]
    return return_string



if __name__ == '__main__':
    s = input()
    print(solve(s))

