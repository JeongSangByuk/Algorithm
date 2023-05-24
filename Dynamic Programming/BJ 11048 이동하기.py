import math
import sys
from collections import deque, defaultdict
import itertools
from heapq import heappush, heappop

n, m = map(int, input().split())

g = list(list(map(int, input().split())) for _ in range(n))

dp = list([0] * m for _ in range(n))

dp[0][0] = g[0][0]

for i in range(1, m):
    dp[0][i] = g[0][i] + dp[0][i - 1]

for i in range(1, n):
    dp[i][0] = g[i][0] + dp[i - 1][0]

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = g[i][j] + max(dp[i-1][j],dp[i][j - 1])

print(dp[n-1][m-1])

