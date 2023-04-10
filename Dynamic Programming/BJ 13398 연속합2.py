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
dp = list([0] * 2 for _ in range(n))

dp[0][0] = g[0]
dp[0][1] = 0

for i in range(1, n):
    dp[i][0] = max(dp[i - 1][0] + g[i], g[i])
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + g[i])

if n == 1:
    print(dp[0][0])
else:
    a, b = zip(*dp)
    print(max(max(a), max(b[1:])))
