import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

input = sys.stdin.readline
n, m = map(int, input().split())
g = list(list(map(int, input().split())) for _ in range(n))
cctv = defaultdict(list)

for i in range(n):
    for j in range(m):
        if 1 <= g[i][j] < 6:

            if g[i][j] == 1 or g[i][j] == 3 or g[i][j] == 4:
                cctv[(i, j)].append((g[i][j], 0))
                cctv[(i, j)].append((g[i][j], 1))
                cctv[(i, j)].append((g[i][j], 2))
                cctv[(i, j)].append((g[i][j], 3))
            elif g[i][j] == 2:
                cctv[(i, j)].append((g[i][j], 0))
                cctv[(i, j)].append((g[i][j], 1))
            elif g[i][j] == 5:
                cctv[(i, j)].append((g[i][j], 0))

cg = list(cctv.keys())
cl = len(cg)
visit = []

dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]


def one(k, g, y, x):
    ny, nx = y, x
    while True:
        ny += dy[k]
        nx += dx[k]

        if not (0 <= ny < n and 0 <= nx < m):
            return

        if g[ny][nx] == 6:
            return
        if 1 <= g[ny][nx] < 6:
            continue
        else:
            g[ny][nx] = -1


def two(k, g, y, x):

    if k == 0:
        one(0, g, y, x)
        one(2, g, y, x)
    else:
        one(1, g, y, x)
        one(3, g, y, x)


def three(k, g, y, x):

    if k == 0:
        one(0, g, y, x)
        one(1, g, y, x)
    elif k == 1:
        one(1, g, y, x)
        one(2, g, y, x)
    elif k == 2:
        one(2, g, y, x)
        one(3, g, y, x)
    elif k == 3:
        one(3, g, y, x)
        one(0, g, y, x)

def four(k, g, y, x):
    if k == 0:
        one(3, g, y, x)
        one(0, g, y, x)
        one(1, g, y, x)
    elif k == 1:
        one(0, g, y, x)
        one(1, g, y, x)
        one(2, g, y, x)
    elif k == 2:
        one(1, g, y, x)
        one(2, g, y, x)
        one(3, g, y, x)
    elif k == 3:
        one(2, g, y, x)
        one(3, g, y, x)
        one(0, g, y, x)

def five(k, g, y, x):
    for i in range(4):
        one(i, g, y, x)


def cctv_move(visit):

    tg = list(i[:] for i in g)

    # print(visit)
    for v in visit:
        (t, k), now = v
        y, x = cg[now][0], cg[now][1]
        if t == 1:
            one(k, tg, y, x)
        elif t == 2:
            two(k, tg, y, x)
        elif t == 3:
            three(k, tg, y, x)
        elif t == 4:
            four(k, tg, y, x)
        elif t == 5:
            five(k, tg, y, x)

    ans = 0
    for i in range(n):
        for j in range(m):
            if tg[i][j] == 0:
                ans += 1
    # print(*tg, sep='\n')
    # print(ans)
    # print("---------------")
    return ans


ans = 9e9
# print(cg)

ori_g = list(i[:] for i in g)

def dfs(now):
    global ans

    if now >= cl:
        ans = min(ans, cctv_move(visit))
        return

    for i in cctv[cg[now]]:
        visit.append((i, now))
        dfs(now + 1)
        visit.pop()

dfs(0)
print(ans)
