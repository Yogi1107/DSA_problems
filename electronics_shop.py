#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b, n ,m ):
    max_ = 0
    result = []
    for i in range(n):
        for j in range(m):
            sum_ = keyboards[i] + drives[j]
            if sum_ <= b:
                result.append(sum_)
                
    if result:
        return max(result)
    else:
        return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b, n, m)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
