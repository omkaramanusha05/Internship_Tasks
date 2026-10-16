#Capitalize!
#https://www.hackerrank.com/challenges/capitalize/problem

#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the solve function below.
def solve(s):
    return ' '.join(
        word.capitalize() for word in s.split(' ')
    )
    for char in s:
        if capitalize_next and char.isalpha():
            result.append(char.upper())
            capitalize_next = False
        else:
            result.append(char)

        if char == ' ':
            capitalize_next = True
            
    return ''.join(result)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
