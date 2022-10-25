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

g = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):

        if i == n-1 and j == n-1:
            print(dp[i][j])
            break

        if j + g[i][j] < n:
            dp[i][j + g[i][j]] += dp[i][j]

        if i + g[i][j] < n:
            dp[i + g[i][j]][j] += dp[i][j]




























