import math
import sys
from collections import deque, defaultdict
import itertools
from heapq import heappush, heappop

n, k = map(int, input().split())

# https://mygumi.tistory.com/135

mod = 1000000000
dp = list([0] * (k + 1) for _ in range(n + 1))

for i in range(n + 1):
    dp[i][1] = 1

for i in range(1, k + 1):
    dp[0][i] = 1

# for i in range(1, n + 1):
#     for j in range(1, k + 1):
#         for t in range(i + 1):
#             dp[i][j] += dp[t][j - 1]

# 조금더 최적화
for i in range(1, n + 1):
    for j in range(1, k + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print(*dp, sep="\n")
print(dp[n][k] % mod)
