import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m, k = map(int, input().split())
g = list(list(map(int, input().strip())) for _ in range(n))
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs():
    que = deque()

    visited = list(list([0] * (k + 1) for _ in range(m)) for _ in range(n))
    # print(*visited, sep='\n')
    que.append((0, 0, 0))
    visited[0][0][0] = 1

    while que:

        node = que.popleft()

        if node[0] == n - 1 and node[1] == m - 1:
            return visited[node[0]][node[1]][node[2]]

        for i in range(4):

            ny = node[0] + dy[i]
            nx = node[1] + dx[i]

            if 0 <= ny < n and 0 <= nx < m:

                if g[ny][nx] == 1 and node[2] < k and visited[ny][nx][node[2] + 1] == 0:
                    visited[ny][nx][node[2] + 1] = visited[node[0]][node[1]][node[2]] + 1
                    que.append((ny,nx,node[2] + 1))
                elif g[ny][nx] == 0 and visited[ny][nx][node[2]] == 0:
                    visited[ny][nx][node[2]] = visited[node[0]][node[1]][node[2]] + 1
                    que.append((ny, nx, node[2]))

    return -1

print(bfs())
