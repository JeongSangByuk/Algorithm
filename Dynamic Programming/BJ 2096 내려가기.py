import math
import sys
from collections import deque, defaultdict
import itertools
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input())

g = list(map(int, input().split()))
dp = list(list([0, 9e9] for _ in range(3)) for _ in range(2))

for i in range(3):
    dp[0][i][0] = g[i]
    dp[0][i][1] = g[i]

for i in range(1, n):

    g = list(map(int, input().split()))

    for k in range(3):
        for j in (k - 1, k, k + 1):

            if not (0 <= j < 3):
                continue

            tmp = dp[0][k][0] + g[j]
            dp[1][j][0] = max(dp[1][j][0], tmp)

            tmp = dp[0][k][1] + g[j]
            dp[1][j][1] = min(dp[1][j][1], tmp)

    for k in range(3):
        dp[0][k][0] = dp[1][k][0]
        dp[0][k][1] = dp[1][k][1]
        dp[1][k][0] = 0
        dp[1][k][1] = 9e9


ans = list(zip(*dp[0]))
print(max(ans[0]), min(ans[1]))
