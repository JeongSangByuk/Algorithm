import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())
g = list(map(int, input().split()))

lo, hi = 0, max(g)


def check(i):

    # i만큼 잘랐을때 합
    _sum = 0

    for j in g:
        tmp = j - i
        if tmp > 0:
            _sum += tmp

    # upper bound
    return _sum >= m


while lo + 1 < hi:

    mid = (lo + hi) // 2

    if check(mid):
        lo = mid
    else:
        hi = mid

print(lo)






