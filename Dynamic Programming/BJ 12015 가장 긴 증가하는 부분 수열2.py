import sys
from collections import deque
import itertools
import heapq
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

# https://st-lab.tistory.com/285
# 가장 작은 것을 찾아 대치한다. -> 길이만을 구하는 것이기 때문.
# 최대한 많이 배치될 수 있도록 가능성을 넓히는 과정.

n = int(input())
g = list(map(int, input().split()))
dp = [0]

for i in g:

    if dp[-1] < i:
        dp.append(i)

    else:
        # lo, hi = 0, len(dp)
        #
        # while lo + 1 < hi:
        #     mid = (lo + hi) // 2
        #
        #     if dp[mid] < i:
        #         lo = mid
        #     else:
        #         hi = mid
        #
        # dp[hi] = i

        dp[bisect_left(dp, i)] = i

# print(dp)
print(len(dp) - 1)