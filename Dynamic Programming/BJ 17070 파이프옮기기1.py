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

ans = 0

# 그냥 완탐
def sol1():

    def dfs(y1, x1, y2, x2):

        global ans

        if y2 == n - 1 and x2 == n-1:
            ans += 1

        # 첫번째 case
        if y1 == y2 and x2 - x1 == 1:

            if x2 + 1 < n and g[y2][x2 + 1] == 0:
                dfs(y2, x2, y2, x2 + 1)

            if x2 + 1 < n and y2 + 1 < n and g[y1][x2 + 1] == 0 \
                    and g[y2 + 1][x2 + 1] == 0 and g[y2 + 1][x2] == 0:
                dfs(y2,x2, y2 + 1, x2 + 1)

        # 두번째 case
        if x1 == x2 and y2 - y1 == 1:

            if y2 + 1 < n and g[y2 + 1][x2] == 0:
                dfs(y2, x2, y2 + 1, x2)

            if x2 + 1 < n and y2 + 1 < n and g[y2][x2 + 1] == 0 \
                    and g[y2 + 1][x2 + 1] == 0 and g[y2 + 1][x2] == 0:
                dfs(y2,x2, y2 + 1, x2 + 1)

        # 세번째 case
        if y2 - y1 == 1 and x2 - x1 == 1:

            if x2 + 1 < n and g[y2][x2 + 1] == 0:
                dfs(y2, x2, y2, x2 + 1)

            if y2 + 1 < n and g[y2 + 1][x2] == 0:
                dfs(y2, x2, y2 + 1, x2)

            if x2 + 1 < n and y2 + 1 < n and g[y2][x2 + 1] == 0 \
                    and g[y2 + 1][x2 + 1] == 0 and g[y2 + 1][x2] == 0:
                dfs(y2, x2, y2 + 1, x2 + 1)

    dfs(0,0,0,1)
    print(ans)

# dp
def sol2():
    dp = [[[0] * n for _ in range(n)] for _ in range(3)]

    # 첫 시작
    dp[0][0][1] = 1

    # 첫 행 초기화
    for i in range(2 ,n):
        if g[0][i] == 0:
            dp[0][0][i] = dp[0][0][i-1]

    for i in range(1, n):
        for j in range(1, n):

            # 현 위치 대각선
            if g[i][j] == 0 and g[i][j - 1] == 0 and g[i - 1][j] == 0:
                dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]

            if g[i][j] == 0:

                # 현 위치 가로
                dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]

                # 현 위치 세로
                dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]

    print(sum(dp[i][n - 1][n - 1] for i in range(3)))

sol2()

