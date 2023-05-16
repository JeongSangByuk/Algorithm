import math
import sys
from collections import deque, defaultdict
import itertools
from heapq import heappush, heappop

input = sys.stdin.readline

n, k = map(int, input().split())
g = list(map(int, input().split()))

_max = sum(g[:k])
tmp = _max

for i in range(k, n):
    tmp += (g[i] - g[i - k])
    _max = max(_max, tmp)

print(_max)