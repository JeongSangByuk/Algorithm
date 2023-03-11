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
start = 0
end = 0

result = 9e9

for start in range(n):

    while end < n and _sum < m:
        _sum += g[end]
        end += 1

    _len = end - start
    if _sum >= m and result > _len:
        result = _len

    _sum -= g[start]

result = 0 if result == 9e9 else result
print(result)



