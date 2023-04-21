import math
import sys
from collections import deque
from collections import defaultdict
import itertools
from heapq import heappush, heappop
from bisect import bisect_left

# https://aerocode.net/392

input = sys.stdin.readline

n = int(input())
g = list(map(int, input().split()))

g.sort()

# print(g)

_sum = 0

l_g = len(g)
for i in range(l_g):

    if _sum + 1 >= g[i]:
        _sum += g[i]
        continue
    break

print(_sum + 1)
