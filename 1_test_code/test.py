import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n+1)]
m = [[0,0]]

for i in range(n):
    m.append(list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w = m[i][0]
        v = m[i][1]

        if w <= j:
            dp[i][j] = max(dp[i-1][j-w] + v, dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][k])

























