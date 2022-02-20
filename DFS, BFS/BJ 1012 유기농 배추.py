import sys
import heapq
from collections import deque, defaultdict
import itertools

input = sys.stdin.readline

k = int(input())

answer = []

# 상하좌우
dy, dx = [1,-1,0,0], [0,0,-1,1]

def solution(m,n,b) :

    cnt = 0
    g = [[0]*m for _ in range(n)]

    for i in range(b):
        x, y = map(int, input().split())
        g[y][x] = 1

    def bfs(i,j):

        que = deque()
        que.append((i,j))
        g[i][j] = 2

        while que :

            # node[0] = y, node[1] =x
            node = que.popleft()

            for t in range(4):

                t_y = node[0] + dy[t]
                t_x = node[1] + dx[t]

                if t_y < 0 or t_y >= n:
                    continue

                if t_x < 0 or t_x >= m:
                    continue

                if g[t_y][t_x] == 1:
                    g[t_y][t_x] = 2
                    que.append((t_y, t_x))

    for i in range(n):
        for j in range(m):
            if g[i][j] == 1:
                cnt += 1
                bfs(i,j)

    answer.append(str(cnt))

for i in range(k):
    m, n, b = map(int, input().split())
    solution(m,n,b)

print(' '.join(answer))

