import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
g = list(map(int, input().split()))

_sum = 0
end = 0
cnt = 0

for start in range(n):

    while end < n and _sum < m:
        _sum += g[end]
        end += 1

    if _sum == m:
        cnt += 1

    _sum -= g[start]

print(cnt)
