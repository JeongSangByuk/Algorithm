import sys
import heapq
from collections import deque, defaultdict
import itertools

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())

g = [list(input().strip()) for _ in range(n)]
g_2 = g[:]

dy, dx = [-1,1,0,0],[0,0,1,-1]

visited = set()
answer = []

def dfs(y, x , color,g):

    for i in range(4):

        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0<= nx < n and not (ny,nx) in visited\
                and color == g[ny][nx]:
            visited.add((ny,nx))
            dfs(ny,nx,color,g)

cnt = 0

for i in range(n):
    for j in range(n):

        if not (i,j) in visited:
            dfs(i,j,g[i][j],g)
            cnt += 1

answer.append(str(cnt))

visited = set()
cnt = 0
# 적록 색약

for i in range(n):
    for j in range(n):
        if g_2[i][j] == 'G':
            g_2[i][j] = 'R'

for i in range(n):
    for j in range(n):

        if not (i,j) in visited:
            dfs(i,j,g_2[i][j],g_2)
            cnt += 1

answer.append(str(cnt))

print(' '.join(answer))


