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
v = [0]
v += list(map(int, input().split()))

g = defaultdict(list)

for i in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited = [False] * (n + 1)
dp = [[0,0] for _ in range(n + 1)]

# 각각의 정점들마다, case를 나눠서 path를 저장하기 위함.
path = [[[], []] for _ in range(n + 1)]

def dfs(start):

    visited[start] = True

    # 선택되는 경우에
    path[start][1].append(start)

    # 선택된다면 최대값
    dp[start][1] = v[start]

    for i in g[start]:

        if not visited[i]:

            dfs(i)

            # 선택했다면, 인접 노드는 선택x여야함.
            dp[start][1] += dp[i][0]

            # 그동안의 루트 더하기
            path[start][1] += path[i][0]

            # 선택안했다면, 인접 노드는 선택하든말든 둘다 되기 때문에 max로

            # 자식 선택하는 경우의 수
            if dp[i][0] < dp[i][1]:

                dp[start][0] += dp[i][1]

                # 그동안의 루트 더하기
                path[start][0] += path[i][1]

            # 자식 선택 안하는 경우의 수
            else:
                dp[start][0] += dp[i][0]

                # 그동안의 루트 더하기
                path[start][0] += path[i][0]

dfs(1)

if dp[1][0] > dp[1][1]:
    i = 0
else:
    i = 1

print(dp[1][i])
path[1][i].sort()
print(*path[1][i], sep=" ")







