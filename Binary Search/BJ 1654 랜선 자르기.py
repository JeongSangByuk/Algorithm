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

g.sort()

def search():
    start = 1
    end = g[-1]

    while start <= end:

        mid = (start + end)//2

        tmp = 0
        for i in range(k):
            tmp += g[i] // mid

        if tmp >= n:
            start = mid + 1
        else:
            end = mid - 1

    return end

def search2():

    def check(mid):

        _sum = 0
        for i in range(k):
            _sum += (g[i] // mid)

        return _sum >= n

    lo, hi = 0, g[-1]

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if check(mid):
            lo = mid
        else:
            hi = mid

    print(lo)





print(search())










