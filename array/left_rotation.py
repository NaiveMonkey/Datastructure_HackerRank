#!/bin/python3

import os
import sys

n = 5
d = 4

a = [1, 2, 3, 4, 5]
b = []
for i in range(n):
    b.append(str(a[(i + d) % n]))
print(' '.join(b))

# if __name__ == '__main__':
#     nd = input().split()
#
#     n = int(nd[0])
#
#     d = int(nd[1])
#
#     a = list(map(int, input().rstrip().split()))
