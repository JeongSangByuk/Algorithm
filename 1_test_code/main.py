import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

# sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())
g = list(map(int, input().split()))

_sum = 0
end = 0
ans = 0

for start in range(n):

    while _sum < m and end < n:

        _sum += g[end]
        end += 1

    if _sum == m:
        ans += 1

    g[start]






























