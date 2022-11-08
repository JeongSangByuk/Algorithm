import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline

n = int(input())
g = list(map(int,input().split()))
g.sort()

def solution():
    m = 9e9
    a1, a2, a3 = 0, 0, 0

    for i in range(n-2):

        start = i + 1
        end = n - 1

        while start < end:

            s = g[start] + g[end] + g[i]

            if abs(s) < m:
                m = abs(s)
                a1, a2, a3 = g[i], g[start], g[end]

            if s < 0:
                start += 1
            elif s > 0:
                end -= 1
            else:
                print(a1,a2,a3)
                return

    print(a1, a2, a3)

solution()







