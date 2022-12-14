import math
import sys
from collections import deque
import itertools
import heapq
from bisect import bisect_left

# sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

dy, dx = [1,-1,0,0], [0,0,-1,1]

def sol(k ,n):

    g = list(list(map(int, input().split())) for _ in range(n))

    que = []

    visited = list([2e9] * n for _ in range(n))

    heapq.heappush(que,(g[0][0],0,0))
    visited[0][0] = g[0][0]

    while que:

        cnt, y, x = heapq.heappop(que)

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if not(0 <= ny < n and 0 <= nx < n):
                continue

            if visited[y][x] + g[ny][nx] < visited[ny][nx]:

                heapq.heappush(que,(visited[y][x] + g[ny][nx], ny, nx))
                visited[ny][nx] = visited[y][x] + g[ny][nx]

    # print(visited)
    print("Problem " + str(k) + ":", visited[n-1][n-1])

k = 1
while True:
    n = int(input())

    if n == 0:
        break

    sol(k, n)
    k += 1






























