import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
g = list(map(int, input().split()))

dp = [0] * n
dp[0] = g[0]

for i in range(1, n):
    dp[i] = max(dp[i - 1] + g[i], g[i])

print(max(dp))
