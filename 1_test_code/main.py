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

n, m = map(int, input().split())
g = list(int(input()) for i in range(m))
g.sort()

def check(mid):
    cnt = 0

    for i in g:
        if i % mid == 0:
            cnt += i // mid
        else:
            cnt += (i//mid) + 1

    return cnt <= n

lo, hi = 0, g[m-1]

while lo + 1 < hi:
    mid = (lo + hi) // 2

    if not check(mid):
        lo = mid
    else:
        hi = mid

print(hi)






