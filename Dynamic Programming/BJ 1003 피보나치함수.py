import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline


fiboarr = [[-1, -1] for _ in range(41)]
max_num = -1
n = int(input())

for y in range(n):

    k = int(input())

    if k < max_num:
        print(fiboarr[k][0], fiboarr[k][1])

    else:

        for i in range(max_num, k + 1):

            if i == 0:
                fiboarr[0][0] = 1
                fiboarr[0][1] = 0

            elif i == 1:
                fiboarr[1][0] = 0
                fiboarr[1][1] = 1

            else:
                fiboarr[i][0] = fiboarr[i - 1][0] + fiboarr[i - 2][0]
                fiboarr[i][1] = fiboarr[i - 1][1] + fiboarr[i - 2][1]
        print(fiboarr[k][0], fiboarr[k][1])
        max_num = k
