import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

# https://blog.naver.com/jinhan814/222607789392

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
g1 = list(map(int, input().split()))

m = int(input())
g2 = list(map(int, input().split()))

g1.sort()

# 직접 구현
def bs(x):

    lo, hi = -1, n

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if not(g1[mid] >= x):
            lo = mid
        else:
            hi = mid

    return hi < n and g1[hi] == x

# bisect 모듈 활용
def bs2(x):
    t = bisect_left(g1, x)

    if t >= n:
        return 0

    return g1[bisect_left(g1,x)] == x

ans = list(1 if bs(i) else 0 for i in g2)
ans2 = list(1 if bs2(i) else 0 for i in g2)

print(*ans2, sep=' ')



