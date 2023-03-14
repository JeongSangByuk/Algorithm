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

    # 처음으로 g[mid]가 k보다 작아지는 시점
    return k <= g[mid]


def bs_lower_bound():
    left = -1
    right = len(g)

    while left + 1 < right:

        mid = (left + right) // 2

        if not check_lower(mid):
            left = mid
        else:
            right = mid

    return right


def check_upper(mid):


    return k < g[mid]


def bs_upper_bound():
    left = 0
    right = len(g)

    while left + 1 < right:

        mid = (left + right) // 2

        if not check_upper(mid):
            left = mid
        else:
            right = mid

    return right


print(bs_lower_bound())
print(bs_upper_bound())





