import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline

k, n = map(int, input().split())

g = [int(input()) for _ in range(k)]

# 몇센치로 자를것인가?
lo, hi = 0, max(g) + 1

def check(mid):

    _sum = 0

    for i in g:
        _sum += i // mid

    # TF
    return _sum >= n

while lo + 1 < hi:

    mid = (lo + hi) // 2

    # TF 분포
    if check(mid):
        lo = mid
    else:
        hi = mid

print(lo)

