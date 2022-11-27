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

g = [int(input()) for _ in range(n)] + [0] * (10000 - n)

dp = [0] * 10000
dp[0] = g[0]
dp[1] = g[0] + g[1]
dp[2] = max(g[0] + g[2], g[1] + g[2], dp[1])

for i in range(3, n):

    a = dp[i - 2] + g[i]
    b = dp[i - 3] + g[i - 1] + g[i]
    c = dp[i - 1]

    dp[i] = max(a,b,c)

print(max(dp))

