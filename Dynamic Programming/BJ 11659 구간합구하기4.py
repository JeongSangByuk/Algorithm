import math
import sys
from collections import deque, defaultdict
import itertools
from heapq import heappush, heappop

input = sys.stdin.readline

n, m = map(int, input().split())
g = list(map(int, input().split()))
c = list(list(map(int, input().split())) for _ in range(m))

dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = dp[i - 1] + g[i - 1]

for i in range(m):
    b, a = c[i][1], c[i][0] - 1
    print(dp[b] - dp[a])
