import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
g = [int(input()) for _ in range(n)] + [0] * 10000

# dp 배열 -> 해당 계단을 밟았을 때의 최댓값
dp = [0] * (10000 + 1)
dp[0] = g[0]
dp[1] = g[0] + g[1]
dp[2] = max(g[0], g[1]) + g[2]

result = 0
for i in range(3, n + 1):
    dp[i] = max(dp[i - 3] + g[i - 1], dp[i - 2]) + g[i]

print(dp[n - 1])
