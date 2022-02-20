import sys
import heapq
from collections import deque, defaultdict
import itertools

input = sys.stdin.readline

answer = []

# 상하좌우
dy, dx = [1,-1,0,0,1,1,-1,-1], [0,0,-1,1,1,-1,-1,1]

while True:

    w, h = map(int, input().split())

    if w == 0 and h == 0 :
        break

    g = [list(map(int, input().split())) for _ in range(h)]

    def bfs(i,j):
        que = deque()
        que.append((i,j))
        g[i][j] = 2

        while que :

            # node[0] = y, node[1] =x
            node = que.popleft()

            for t in range(8):

                t_y = node[0] + dy[t]
                t_x = node[1] + dx[t]

                if t_y < 0 or t_y >= h:
                    continue

                if t_x < 0 or t_x >= w:
                    continue

                if g[t_y][t_x] == 1:
                    g[t_y][t_x] = 2
                    que.append((t_y, t_x))

    cnt = 0

    for i in range(h):
        for j in range(w):
            if g[i][j] == 1:
                cnt += 1
                bfs(i, j)

    answer.append(str(cnt))

print('\n'.join(answer))