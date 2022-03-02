import sys
import heapq
from collections import deque, defaultdict
import itertools

sys.setrecursionlimit(10**7)

input = sys.stdin.readline

m,n = map(int, input().split())

g = [list(map(int, input().split())) for _ in range(n)]

dy, dx = [-1, 1, 0 , 0], [0,0,1,-1]

answer = 0

def bfs(l) :

    global answer

    que = deque(l)

    while que:

        # (y,x, cnt)
        node = que.popleft()

        for i in range(4):

            ny = node[0] + dy[i]
            nx = node[1] + dx[i]
            cnt = node[2]

            if 0 <= ny < n and 0 <= nx < m and g[ny][nx] == 0 :
                g[ny][nx] = 1
                que.append((ny,nx,cnt + 1))

                if answer < cnt + 1:
                    answer = cnt + 1

point = []

# 토마토가 있는 point 찾기
for i in range(n):
    for j in range(m):

        if g[i][j] == 1:
            point.append((i,j,0))

bfs(point)

# 만약 bfs를 다돌았는데도 0이 남아 있는 경우
for i in range(n):
    for j in range(m):

        if g[i][j] == 0:
            answer = -1
            break

print(answer)