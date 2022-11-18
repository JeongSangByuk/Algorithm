import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
g = defaultdict(list)

for i in range(m):
    a,b,c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))

def bfs2():

    t = 2

    que = []
    visited = [9e9] * (n + 1)

    visited[t] = 0

    heapq.heappush(que, (0, t))

    while que:

        w, node = heapq.heappop(que)

        if visited[node] < w:
            continue

        for i in g[node]:
            if visited[i[0]] > w + i[1]:
                heapq.heappush(que, (w + i[1], i[0]))
                visited[i[0]] = w + i[1]

    return visited

visited = bfs2()

def sol(start):

    if dp[start] == 0:
        for i in g[start]:
            if visited[start] > visited[i[0]]:
                dp[start] += sol(i[0])
        return dp[start]

    return dp[start]

dp = [0 for _ in range(n+1)]
dp[2] = 1

print(sol(1))














