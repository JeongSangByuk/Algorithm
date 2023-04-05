import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

input = sys.stdin.readline

n, q = map(int, input().split())
g = list(list(map(int, input().split())) for _ in range(2 ** n))
command = list(map(int, input().split()))

dy, dx = (-1, 1, 0, 0), (0, 0, 1, -1)


def rotate(y, x, l):
    tg = list(i[x:x + 2 ** l] for i in g[y:y + 2 ** l])

    new_tg = list(map(list, zip(*tg[::-1])))

    for i in range(y, y + 2 ** l):
        for j in range(x, x + 2 ** l):
            g[i][j] = new_tg[i - y][j - x]


def check():
    fix = []

    for i in range(2 ** n):
        for j in range(2 ** n):

            cnt = 0

            for k in range(4):

                ny = i + dy[k]
                nx = j + dx[k]

                if not (0 <= ny < 2 ** n and 0 <= nx < 2 ** n):
                    cnt += 1
                    continue

                if g[ny][nx] == 0:
                    cnt += 1

            if cnt > 1:
                fix.append((i, j))

    for f in fix:
        if g[f[0]][f[1]] > 0:
            g[f[0]][f[1]] -= 1


for c in command:

    for i in range(2 ** n // 2 ** c):
        for j in range(2 ** n // 2 ** c):
            # print(i * 2 ** c, j * 2 ** c, c)
            rotate(i * 2 ** c, j * 2 ** c, c)

    check()

visit = set()
s = 0

def bfs(y, x):
    global s
    que = deque()
    tvisit = set()

    que.append((y, x))
    tvisit.add((y,x))

    while que:

        y, x = que.popleft()
        s += g[y][x]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if not (0 <= ny < 2 ** n and 0 <= nx < 2 ** n):
                continue

            if g[ny][nx] == 0 or (ny,nx) in tvisit:
                continue

            que.append((ny, nx))
            tvisit.add((ny, nx))

    return tvisit

ans = 0
for i in range(2 ** n):
    for j in range(2 ** n):

        if (i,j) not in visit and g[i][j] != 0:
            tv = bfs(i, j)
            ans = max(ans, len(tv))
            visit = visit.union(tv)

# s = sum(list(sum(i) for i in g))
# print(*g, sep="\n")
print(s)
print(ans)
