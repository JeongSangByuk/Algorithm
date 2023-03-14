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

def check(mid):

    # mid개 만큼 나눠줄 때 나눠줄 수 있는 사람가 n 이하인가?

    _sum = 0

    for i in g:
        if i % mid == 0:
            _sum += i // mid
        else:
            _sum += (i//mid) + 1

    # 1 2 3 4 7   // mid
    # 9 6 5 5 1     // n명
    # F F T T T
    return _sum <= n

lo, hi = 0, max(g) + 1

while lo + 1 < hi:
    mid = (lo + hi) // 2

    if check(mid):
        hi = mid
    else:
        lo = mid

print(hi)

