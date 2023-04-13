import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n = int(input())
g = list(map(int, input().split()))
dp = [g[0]]

for i in g:

    if dp[-1] < i:
        dp.append(i)
        # print(dp)

        continue

    lo = bisect_left(dp, i)

    dp[lo] = i

    # print(dp)

print(len(dp))

