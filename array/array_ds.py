#!/bin/python3

import os
import sys

#
# Complete the reverseArray function below.
#
def reverse_array(a):
    arr = []
    for i in range(0, len(a)):
        arr.append(a[len(a) - i - 1])
    return arr

print(" ".join(map(str, reverse_array([1,4,3,2]))))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     arr_count = int(input())
#
#     arr = list(map(int, input().rstrip().split()))
#
#     res = reverse_array(arr)
#
#     fptr.write(' '.join(map(str, res)))
#     fptr.write('\n')
#
#     fptr.close()