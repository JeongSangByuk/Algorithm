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

k = 3
g = [1, 2, 3, 3, 3, 4]
g.sort()

print(g)


def check_lower(mid):
    # 처음으로 g[mid]가 k보다 크거나 같아지는 시점을 찾는다
    # 이때 FT 분포이기때문에 hi return
    return g[mid] >= k


def bs_lower_bound():
    lo = -1
    hi = len(g)

    while lo + 1 < hi:

        mid = (lo + hi) // 2

        if not check_lower(mid):
            lo = mid
        else:
            hi = mid

    return hi


def check_upper(mid):
    # 처음으로  g[mid]가 k보다 커지는 시점을 찾는다
    return g[mid] > k


def bs_upper_bound():
    lo = 0
    hi = len(g)

    while lo + 1 < hi:

        mid = (lo + hi) // 2

        if not check_upper(mid):
            lo = mid
        else:
            hi = mid

    return hi


print(bs_lower_bound())
print(bs_upper_bound())
