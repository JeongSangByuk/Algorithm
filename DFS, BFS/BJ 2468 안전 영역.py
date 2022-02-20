import sys
import heapq
from collections import deque, defaultdict
import itertools

input = sys.stdin.readline

# 상하좌우
dy, dx = [1,-1,0,0], [0,0,-1,1]

n = int(input())

g = [list(map(int, input().split())) for _ in range(n)]
g_max = max(map(max,g))
answer = []

def bfs(tmp_g, i, j):

    que = deque()
    que.append((i, j))
    tmp_g[i][j] = 2

    while que:

        # node[0] = y, node[1] =x
        node = que.popleft()

        for t in range(4):

            t_y = node[0] + dy[t]
            t_x = node[1] + dx[t]

            if t_y < 0 or t_y >= n:
                continue

            if t_x < 0 or t_x >= n:
                continue

            if tmp_g[t_y][t_x] == 1:
                tmp_g[t_y][t_x] = 2
                que.append((t_y, t_x))

for k in range(1,g_max):

    tmp_g = [item[:] for item in g]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if tmp_g[i][j] <= k:
                tmp_g[i][j] = 0
            else:
                tmp_g[i][j] = 1

    for i in range(n):
        for j in range(n):
            if tmp_g[i][j] == 1:
                cnt += 1
                bfs(tmp_g, i, j)

    answer.append(cnt)

#print(answer)
print(max(answer))