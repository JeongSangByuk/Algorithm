import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

input = sys.stdin.readline

BLACK_BLOCK = -1
RAINBOW_BLOCK = 0
EMPTY_BLOCK = -2

dy, dx = (-1, 1, 0, 0), (0, 0, 1, -1)

n, m = map(int, input().split())
g = list(list(map(int, input().split())) for _ in range(n))

def bfs(y, x, color):
    que = deque()
    tvisit = set()

    que.append((y, x))
    tvisit.add((y, x))

    while que:

        y, x = que.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if not (0 <= ny < n and 0 <= nx < n):
                continue

            if (ny, nx) in tvisit:
                continue

            if g[ny][nx] != color and g[ny][nx] != RAINBOW_BLOCK:
                continue

            que.append((ny, nx))
            tvisit.add((ny, nx))

    return tvisit

def get_mid(tv):
    min_y, min_x = 9e9, 9e9

    for i in tv:

        if g[i[0]][i[1]] == RAINBOW_BLOCK:
            continue

        min_y = min(min_y, i[0])
        min_x = min(min_x, i[1])

    return min_y, min_x

def cnt_rainbow(tv):
    cnt = 0

    for i in tv:
        if g[i[0]][i[1]] == RAINBOW_BLOCK:
            cnt += 1

    return cnt


def play():
    global ans
    _max = 0
    max_visit = set()
    visit = set()

    # 가장 넓은 분위 겟
    for y in range(n):
        for x in range(n):

            if (y, x) in visit or g[y][x] == BLACK_BLOCK or g[y][x] == RAINBOW_BLOCK or g[y][x] == EMPTY_BLOCK:
                continue

            tv = bfs(y, x, g[y][x])
            visit = visit.union(tv)

            if _max < len(tv):
                max_visit = tv.copy()
                _max = len(tv)
            elif _max == len(tv):

                # 같으면 레인보우 찾기.
                or1 = cnt_rainbow(max_visit)
                or2 = cnt_rainbow(tv)

                if or2 > or1:
                    max_visit = tv.copy()
                    _max = len(tv)

                # 무지개블록 마저 같으면,
                elif or2 == or1:

                    ori_mid_y, ori_mid_x = get_mid(max_visit)
                    mid_y, mid_x = get_mid(tv)

                    if mid_y > ori_mid_y:
                        max_visit = tv.copy()
                    elif mid_y == ori_mid_y:
                        if mid_x > ori_mid_x:
                            max_visit = tv.copy()
    # print(max_visit)
    if len(max_visit) < 2:
        return False

    ans += (len(max_visit) ** 2)
    for v in max_visit:
        g[v[0]][v[1]] = EMPTY_BLOCK

    move()
    return True

def move():
    for x in range(n):
        y = n - 2
        p = n - 1

        while y >= 0:

            if g[p][x] != EMPTY_BLOCK or g[p][x] == BLACK_BLOCK:
                p -= 1
                y -= 1
                continue

            if g[y][x] == EMPTY_BLOCK:
                y -= 1
            elif g[y][x] == BLACK_BLOCK:
                p = y
                y = p - 1
            elif g[y][x] > BLACK_BLOCK:
                g[p][x] = g[y][x]
                g[y][x] = -2

def rotate():
    return list(map(list, zip(*g)))[::-1]

ans = 0

while True:

    # print("now")
    # print(*g, sep="\n", end="\n\n")
    if not play():
        break
    # print("coll")
    # print(*g, sep="\n", end="\n\n")

    move()
    # print("move")
    # print(*g, sep="\n", end="\n\n")

    g = rotate()
    # print("rotate")
    # print(*g, sep="\n", end="\n\n")

    move()
    # print("move")
    # print(*g, sep="\n", end="\n\n")
    # print(ans)
    # print("-------------------")

print(ans)


