import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline

n = int(input())
g = list(list(map(int, input().split())) for i in range(n))

sys.setrecursionlimit(10 ** 6)
dy,dx = [-1,1,0,0],[0,0,-1,1]
dp = [[0] * n for i in range(n)]

def dfs(y,x):

    if dp[y][x]:
        return dp[y][x]

    dp[y][x] = 1

    for i in range(4):

        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < n and g[y][x] < g[ny][nx]:
            dp[y][x] = max(dp[y][x], dfs(ny,nx) + 1)

    return dp[y][x]

answer = 0

for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))


print(answer)




















