#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    rounded = []
    for g in grades:
        gb = math.ceil(g/10) * 10
        mb = gb - 5
        
        if g < 38:
            rounded.append(g)
        elif gb - g < 3:
            rounded.append(gb)
        elif mb - g < 3 and mb - g > 0:
            rounded.append(mb)
        else:
            rounded.append(g)
    
    return rounded

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
