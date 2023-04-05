import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

input = sys.stdin.readline

# left down right up
dy, dx = [0, 1, 0, -1], [-1, 0, 1, 0]

sand_left = [(-2, 0, 0.02), (-1, 0, 0.07), (2, 0, 0.02), (1, 0, 0.07),
             (-1, -1, 0.1), (1, -1, 0.1), (-1, 1, 0.01), (1, 1, 0.01)
    , (0, -2, 0.05)]

sand_right = [(-2, 0, 0.02), (-1, 0, 0.07), (2, 0, 0.02), (1, 0, 0.07),
              (-1, -1, 0.01), (1, -1, 0.01), (-1, 1, 0.1), (1, 1, 0.1)
    , (0, 2, 0.05)]

sand_down = [(0, 2, 0.02), (0, 1, 0.07), (0, -2, 0.02), (0, -1, 0.07),
             (-1, -1, 0.01), (1, -1, 0.1), (-1, 1, 0.01), (1, 1, 0.1)
    , (2, 0, 0.05)]

sand_up = [(0, 2, 0.02), (0, 1, 0.07), (0, -2, 0.02), (0, -1, 0.07),
           (-1, -1, 0.1), (1, -1, 0.01), (-1, 1, 0.1), (1, 1, 0.01)
    , (-2, 0, 0.05)]

sand = [sand_left, sand_down, sand_right, sand_up]

n = int(input())
g = list(list(map(int, input().split())) for _ in range(n))

mid = n // 2

dist = 1


def make_send(y, x, move_type):
    total = 0
    out_total = 0
    send_m = g[y][x]

    for s in sand[move_type]:
        ny = y + s[0]
        nx = x + s[1]

        t = int(round(send_m * s[2], 10))

        total += t

        if not (0 <= ny < n and 0 <= nx < n):
            out_total += t
            continue

        g[ny][nx] += t

    ny = y + dy[move_type]
    nx = x + dx[move_type]
    if 0 <= ny < n and 0 <= nx < n:
        g[ny][nx] += send_m - total
    else:
        out_total += send_m - total

    return out_total


ans = 0
ny, nx = mid, mid
tmp = 0
move_k = 0
move_type = 0

while True:

    is_fin = False

    for _ in range(dist):

        ny += dy[move_type]
        nx += dx[move_type]

        if ny == 0 and nx == -1:
            is_fin = True
            break

        if g[ny][nx] == 0:
            continue

        ans += make_send(ny, nx, move_type)
        # print(ny, nx, ans)
        g[ny][nx] = 0
        # print(*g, sep='\n')
        # print("--------------------")

    if is_fin:
        break

    move_type = (move_type + 1) % 4
    move_k += 1

    if move_k == 2:
        move_k = 0
        dist += 1

# print(*g, sep='\n')
print(ans)
