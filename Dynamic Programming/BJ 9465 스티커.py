import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

k = int(input())
ans = []

for kk in range(k):
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(2)]
    dp = [item[:] for item in g]

    if n != 1:

        dp[0][1] += g[1][0]
        dp[1][1] += g[0][0]

        for i in range(2, n):
            dp[0][i] += max(dp[1][i-2], dp[1][i-1])
            dp[1][i] += max(dp[0][i-2], dp[0][i-1])

    ans.append(max(dp[0][n-1],dp[1][n-1]))

print(*ans, sep = '\n')
