import sys
import heapq
from collections import deque, defaultdict
import itertools

sys.setrecursionlimit(100000)

input = sys.stdin.readline

n, m = map(int, input().split())

g = [list(map(int, input().split())) for _ in range(n)]

dy,dx = [-1,1,0,0],[0,0,-1,1]

def dfs(y,x,visited):

    visited.add((y,x))

    # 동서남북 dfs
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        if 0 <= ny < n and 0 <= nx < m:

            if g[ny][nx] != 0 and (ny,nx) not in visited:
                dfs(ny,nx,visited)

answer = 0

while True:

    answer += 1

    tmp_g = [item[:] for item in g]

    for i in range(n):
        for j in range(m):

            if g[i][j] != 0:

                # 동서남북 빙하 녹이기
                for k in range(4):

                    ny = i + dy[k]
                    nx = j + dx[k]

                    if 0 <= ny < n and 0 <= nx < m:
                        if g[ny][nx] == 0:
                            tmp_g[i][j] -= 1

                    if tmp_g[i][j] == 0:
                        break
    g = tmp_g[:]

    cnt = 0
    visited = set()

    for i in range(n):
        for j in range(m):

            if g[i][j] != 0 and (i,j) not in visited:
                dfs(i,j,visited)
                cnt += 1

    #print(cnt)

    if cnt > 1:
        print(answer)
        break

    elif cnt == 0:
        print(0)
        break







