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

g = []
cost = []
dp = [0 for _ in range(n + 1)]

for i in range(n):
    a, b = map(int, input().split())
    g.append(a)
    cost.append(b)

_max = 0

for i in range(n):
    _max = max(_max, dp[i])

    if i + g[i] > n:
        continue

    dp[i + g[i]] = max(dp[i + g[i]], _max + cost[i])

print(max(dp))




