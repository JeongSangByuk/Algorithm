import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

x, y, c = map(float, input().split())

lo, hi = 0, min(x,y)

def check(mid):

    h1 = math.sqrt(x * x - mid * mid)
    h2 = math.sqrt(y * y - mid * mid)

    return c <= ((h1 * h2) / (h1 + h2))

while abs(hi - lo) > 1e-6:

    mid = (lo + hi) / 2.0

    if check(mid):
        lo = mid
    else:
        hi = mid

print("%.3f" %round(lo,3))