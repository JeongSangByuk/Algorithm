import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
g = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = g[i]

for i in range(2, n + 1):

    tmp = list()

    t = i // 2

    for j in range(1, t + 1):
        dp[i] = max(dp[i], dp[j] + dp[i - j])

print(dp[n])

