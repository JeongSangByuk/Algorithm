import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

input = sys.stdin.readline

n = 4
SHARP = -1
dy, dx = (-1, -1, 0, 1, 1, 1, 0, -1), (0, -1, -1, -1, 0, 1, 1, 1)
g = list(list() for _ in range(4))

# key 물고기 번호
# value = [y, x, 방향]
fish = dict()

for i in range(n):
    tg = list(map(int, input().split()))

    for j in range(n):
        g[i].append([tg[j * 2], tg[j * 2 + 1] - 1])

for y in range(n):
    for x in range(n):
        fish[g[y][x][0]] = [y, x, g[y][x][1]]


def rotate_fish(new_g, new_fish):

    for i in range(1, n * n + 1):

        if i not in new_fish.keys():
            continue

        y, x, d = new_fish[i]

        if new_g[y][x][0] == SHARP or new_g[y][x][0] == 0:
            continue

        cnt = 1
        while cnt < 9:

            d = d % 8
            ny = y + dy[d]
            nx = x + dx[d]

            # 벗어나거나 OR 상어
            if not (0 <= ny < n and 0 <= nx < n) or new_g[ny][nx][0] == SHARP:
                d = d + 1
                cnt += 1
                continue

            # 바꾸기

            of = new_g[y][x][0]
            tf = new_g[ny][nx][0]

            if tf != 0:

                new_fish[tf] = [y, x, new_fish[tf][2]]
                new_fish[of] = [ny, nx, d]

                new_g[y][x][0], new_g[y][x][1] = tf, new_fish[tf][2]
                new_g[ny][nx][0], new_g[ny][nx][1] = of, d

            # 빈칸인 경우
            elif tf == 0:
                # new_fish[tf] = [y, x, new_fish[tf][2]]
                new_fish[of] = [ny, nx, d]

                new_g[y][x][0] = 0
                new_g[ny][nx][0], new_g[ny][nx][1] = of, d

            break

        # print("물고기 이동", i)
        # print(*new_g, sep="\n", end="\n\n")

    return new_g, new_fish


que = deque()
que.append((0, 0, g[0][0][1], g[0][0][0], g, fish))

on = g[0][0][0]
g[0][0][0] = SHARP

fish.pop(on, None)
rotate_fish(g, fish)

ans = 0
while que:
    y, x, d, cnt, tg, tf = que.popleft()

    # print(y,x)

    ans = max(ans, cnt)
    # print(ans)
    # print(*tg, sep="\n", end="\n\n")

    k = 1
    while True:

        ny = y + dy[d] * k
        nx = x + dx[d] * k

        if not (0 <= ny < n and 0 <= nx < n):
            break

        if tg[ny][nx][0] == 0:
            k += 1

            continue

        on = tg[ny][nx][0]
        od = tg[ny][nx][1]
        tcnt = cnt + tg[ny][nx][0]

        new_g = list(list() for _ in range(4))
        new_fish = dict()
        for tff in tf:
            new_fish[tff] = tf[tff][:]

        for i in range(n):
            for j in range(n):
                new_g[i].append(tg[i][j][:])

        new_g[y][x][0] = 0
        new_g[ny][nx][0] = SHARP
        new_fish.pop(on, None)

        new_g, new_fish = rotate_fish(new_g, new_fish)

        que.append((ny, nx, od, tcnt, new_g, new_fish))
        k += 1

print(ans)