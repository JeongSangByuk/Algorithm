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
g.sort()

left, right = 0, g[n - 1]

# mid 높이에 절단기를 위치했을때, m이상의 나무를 얻을 수 있는가?
# TF 분포, True가 되는 시점이 중요
def check(mid):
    _sum = 0

    for i in g:
        if (i > mid):
            _sum += (i - mid)

    # 즉, _sum의 값이 m 보다 커질 때를 찾는다.
    return _sum >= m

while left + 1 < right:

    mid = (left + right) // 2

    if check(mid):
        left = mid
    else:
        right = mid

print(left)


