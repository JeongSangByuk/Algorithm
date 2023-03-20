import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
k = int(input())

# 결국 lo, hi를 잡고 check(lo) != check(hi)가 되는
# 시점을 찾는 결정함수를 잘 짜는 것이 중요하다.
# k와 정답간의 관계 파악하기.

def check(mid):

    cnt = 0

    for i in range(1, n + 1):
        cnt += min(mid//i, n)

    # cnt = mid 보다 작거나 같은 칸의 개수
    # cnt가 k보다 크거나 같
    return cnt >= k

lo, hi = 0, n*n + 1

while lo + 1 < hi:

    mid = (lo + hi) // 2

    if check(mid):
        hi = mid
    else:
        lo = mid

print(hi)

