import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

input = sys.stdin.readline

n, m = map(int, input().split())
g = [int(input()) for _ in range(n)]

# 26  27 28 29 30
#  5  5   6 6  6
#  f  f   t  t

def check(mid):

    # FT
    _sum = 0

    for i in g:
        _sum += mid//i

    return m <= _sum


lo = 0
hi = max(g) * m + 1

while lo + 1 < hi:
    mid = (lo + hi) // 2

    if check(mid):
        hi = mid
    else:
        lo = mid

print(hi)






