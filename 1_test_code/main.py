import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
g = list(map(int, input().split()))
dp = [0]

for i in g:

    if dp[-1] < i:
        dp.append(i)
        print(dp)

        continue

    # lo = bisect_left(dp, i)

    lo, hi = 0, len(dp)

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if dp[mid] < i:
            lo = mid
        else:
            hi = mid

    dp[hi] = i

    print(dp)

print(len(dp) - 1)