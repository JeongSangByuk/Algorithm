import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

g = list(list(map(str, input().strip())) for _ in range(12))
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(y, x, visited):
    tvisited = set()

    que = deque()
    tvisited.add((y, x))
    que.append((y, x))
    ori_color = g[y][x]
    cnt = 0

    while que:

        ny, nx = que.popleft()
        cnt += 1

        for i in range(4):
            ty, tx = ny + dy[i], nx + dx[i]
            if 0 <= ty < 12 and 0 <= tx < 6 and (ty, tx) not in tvisited and g[ty][tx] == ori_color:
                que.append((ty, tx))
                tvisited.add((ty, tx))

    if cnt < 4:
        return False

    for i in tvisited:
        g[i[0]][i[1]] = '.'

    visited.union(tvisited)

    return True


def change():
    for i in range(6):
        dot_cnt = 0
        for j in range(11, -1, -1):

            if g[j][i] == '.':
                dot_cnt += 1
                continue
            if dot_cnt > 0:
                g[j + dot_cnt][i] = g[j][i]
                g[j][i] = '.'

result = 0


def sol():
    global result
    visited = set()

    tmp = 0

    for i in range(11, -1, -1):
        for j in range(6):
            if g[i][j] != '.' and (i, j) not in visited:

                if bfs(i, j, visited):
                    tmp += 1


    if tmp == 0:
        return False

    change()
    result += 1
    return True


while True:

    if not sol():
        break

    # print(*g, sep='\n')
    # print("----")

print(result)
