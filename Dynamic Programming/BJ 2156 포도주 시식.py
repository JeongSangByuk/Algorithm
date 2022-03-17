import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())

g = list(int(input()) for _ in range(n)) + [0] * (10000 - n)
dp = [0] * 10000

dp[0] = g[0]
dp[1] = g[0] + g[1]
dp[2] = max(g[0] + g[2], g[1] + g[2], dp[1])

for i in range(3, n):
    dp[i] = max(dp[i-2] + g[i], dp[i - 3] + g[i-1] + g[i], dp[i - 1])

print(max(dp))