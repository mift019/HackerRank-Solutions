import math
import os
import random
import re
import sys

# Function Solutions
def MinMaxSum(ar):
    sum = 0
    for i in range (len(ar)):
        sum += ar[i]
    print(sum-min(ar), sum-max(ar))

if __name__ == '__main__':
    ar = list(map(int, input().rstrip().split()))
    MinMaxSum(ar)
