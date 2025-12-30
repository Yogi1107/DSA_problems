#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    from collections import Counter
    
    freq = Counter(s)
    freq_values = list(freq.values())
    
    freq_count = Counter(freq_values)
    
    if len(freq_count) == 1:
        return "YES"
    
    if len(freq_count) == 2:
        (f1, c1), (f2, c2) = freq_count.items()
        
        # Case 1: one character appears once
        if (f1 == 1 and c1 == 1) or (f2 == 1 and c2 == 1):
            return "YES"
        
        # Case 2: one character has one extra occurrence
        if abs(f1 - f2) == 1:
            if (f1 > f2 and c1 == 1) or (f2 > f1 and c2 == 1):
                return "YES"
    
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
