import sys
import heapq
from collections import deque, defaultdict
import itertools

sys.setrecursionlimit(10**7)

input = sys.stdin.readline

m,n,h = map(int, input().split())

g = []

for i in range(h):
    g.append([list(map(int, input().split())) for _ in range(n)])

dz, dy, dx = [-1, 1, 0 ,0,0,0], [0,0,1,-1,0,0], [0,0,0,0,-1,1]

answer = 0

def bfs(l) :

    global answer

    que = deque(l)

    while que:

        # (z, y,x, cnt)
        node = que.popleft()

        for i in range(6):

            nz = node[0] + dz[i]
            ny = node[1] + dy[i]
            nx = node[2] + dx[i]
            cnt = node[3]

            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and g[nz][ny][nx] == 0 :
                g[nz][ny][nx] = 1
                que.append((nz,ny,nx,cnt + 1))

                if answer < cnt + 1:
                    answer = cnt + 1

# z,y,x
point = []

# 토마토가 있는 point 찾기
for z in range(h):
    for i in range(n):
        for j in range(m):

            if g[z][i][j] == 1:
                point.append((z,i,j,0))

bfs(point)

# 만약 bfs를 다돌았는데도 0이 남아 있는 경우
for z in range(h):
    for i in range(n):
        for j in range(m):

            if g[z][i][j] == 0:
                answer = -1
                break

print(answer)