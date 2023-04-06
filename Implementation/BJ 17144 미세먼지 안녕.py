import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

input = sys.stdin.readline

dy, dx = (-1, 1, 0, 0), (0, 0, 1, -1)

n, m, t = map(int, input().split())
g = list(list(map(int, input().split())) for _ in range(n))
robot = []

for i in range(n):
    for j in range(m):
        if g[i][j] == -1:
            robot.append(i)


def spread():
    dic = defaultdict(int)

    for y in range(n):
        for x in range(m):

            if g[y][x] <= 0:
                continue

            s = 0

            t = g[y][x] // 5

            if t == 0:
                continue

            cnt = 0

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if not (0 <= ny < n and 0 <= nx < m) or g[ny][nx] == - 1:
                    continue

                dic[(ny, nx)] += t
                cnt += 1

            dic[(y, x)] -= (t * cnt)

    for i in dic:
        g[i[0]][i[1]] += dic[i]


def move():
    tmp_00 = g[0][0]
    for i in range(m - 1):
        g[0][i] = g[0][i + 1]

    tmp_r1 = g[robot[0]][m - 1]
    for i in range(m - 1, 1, -1):
        g[robot[0]][i] = g[robot[0]][i - 1]
    g[robot[0]][1] = 0

    # 아래로
    for i in range(robot[0] - 1, 1, -1):
        g[i][0] = g[i - 1][0]
    g[1][0] = tmp_00

    for i in range(robot[0]):
        g[i][m - 1] = g[i + 1][m - 1]
    g[robot[0] - 1][m - 1] = tmp_r1

    ##

    # 좌로
    tmp_00 = g[n - 1][0]
    for i in range(m - 1):
        g[n - 1][i] = g[n - 1][i + 1]

    # 우로
    tmp_r1 = g[robot[1]][m - 1]
    for i in range(m - 1, 1, -1):
        g[robot[1]][i] = g[robot[1]][i - 1]
    g[robot[1]][1] = 0

    # 아래로
    for i in range(n - 1, robot[1], -1):
        g[i][m - 1] = g[i - 1][m - 1]
    g[robot[1] + 1][m - 1] = tmp_r1

    # 위로
    for i in range(robot[1] + 1, n - 1):
        g[i][0] = g[i + 1][0]
    g[n - 2][0] = tmp_00


for i in range(t):
    spread()
    # print(*g, sep="\n",end="\n\n")

    move()
    # print(*g, sep="\n")

ans = 0
for i in range(n):
    for j in range(m):
        ans += g[i][j]

print(ans + 2)
