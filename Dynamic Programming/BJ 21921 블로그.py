import math
import sys
from collections import deque, defaultdict
import itertools
from heapq import heappush, heappop

input = sys.stdin.readline

n, x = map(int, input().split())
g = list(map(int, input().split()))

_max = sum(g[:x])
tmp = _max
ans = 1

for i in range(x, n):
    tmp += (g[i] - g[i - x])

    if tmp == _max:
        ans += 1
        continue

    if _max < tmp:
        ans = 1
        _max = tmp

if _max == 0:
    print("SAD")
else:
    print(_max)
    print(ans)
