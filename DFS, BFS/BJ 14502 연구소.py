import copy
import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n,m = map(int, input().split())

g = [list(map(int, input().split())) for _ in range(n)]

visited = [[-1]*m for _ in range(n)]

dy,dx=[0,1,0,-1],[1,0,-1,0]

answer = 0

def countSafe():

    cnt = 0
    gg = [item[:] for item in g]

    for i in range(n):
        for j in range(m):
            if gg[i][j] == 2:
                bfs(i,j,gg)

    for i in range(n):
        for j in range(m):
            if gg[i][j] == 0:
                cnt += 1
    return cnt

def bfs(y,x,gg):

    queue = deque()

    queue.append((y,x))

    while queue:

        y,x = queue.popleft()

        for i in range(4):

            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and gg[ny][nx] == 0:

                gg[ny][nx] = 2
                queue.append((ny,nx))

def dfs(y,x, cnt):

    global answer

    if cnt == 3:

        answer = max(answer,countSafe())

        return

    for i in range(n):
        for j in range(m):

            if g[i][j] == 0:

                # 벽 세우기
                g[i][j] = 1
                dfs(i,j,cnt+1)
                g[i][j] = 0


dfs(0,0,0)


#print(g)
print(answer)