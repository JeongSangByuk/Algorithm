import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

input = sys.stdin.readline


def sol1():
    n = int(input())
    g = list(list(map(int, input().split())) for _ in range(n))

    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

    def move_vertical(g, k):
        tmp_g = list(i[:] for i in g)

        for x in range(n):

            y = 0 if k == 0 else n
            tvisit = set()

            while y < n if k == 0 else y >= 0:
                ny = y + dy[k]

                if not (0 <= ny < n):
                    y -= dy[k]
                    continue
                if tmp_g[ny][x] == 0 and tmp_g[y][x] == 0:
                    y -= dy[k]
                    continue

                if tmp_g[ny][x] == 0:
                    tmp_g[ny][x] = tmp_g[y][x]
                    tmp_g[y][x] = 0
                    y = ny
                elif tmp_g[ny][x] == tmp_g[y][x] and (ny, x) not in tvisit and (y, x) not in tvisit:
                    tmp_g[ny][x] *= 2
                    tmp_g[y][x] = 0
                    y = ny
                    tvisit.add((ny, x))
                else:
                    y -= dy[k]

        return tmp_g

    def move_hori(g, k):
        tmp_g = list(i[:] for i in g)

        for y in range(n):

            x = 0 if k == 2 else n
            tvisit = set()

            while x < n if k == 2 else x >= 0:
                nx = x + dx[k]

                if not (0 <= nx < n):
                    x -= dx[k]
                    continue
                if tmp_g[y][nx] == 0 and tmp_g[y][x] == 0:
                    x -= dx[k]
                    continue

                if tmp_g[y][nx] == 0:
                    tmp_g[y][nx] = tmp_g[y][x]
                    tmp_g[y][x] = 0
                    x = nx
                elif tmp_g[y][nx] == tmp_g[y][x] and (y, nx) not in tvisit and (y, x) not in tvisit:
                    tmp_g[y][nx] *= 2
                    tmp_g[y][x] = 0
                    x = nx
                    tvisit.add((y, nx))
                else:
                    x -= dx[k]

        return tmp_g

    def make_visit_ele(tmp_g):
        return tuple(tuple(i) for i in tmp_g)

    def cnt_max(tmp_g):
        return max(max(i) for i in tmp_g)

    que = deque()
    visit = set()

    tmp_g = list(i[:] for i in g)
    que.append((tmp_g, 0))
    visit.add(make_visit_ele(tmp_g))

    result = 0

    while que:

        node_g, cnt = que.popleft()
        # print(node_g, cnt)

        if cnt > 5:
            break

        result = max(result, cnt_max(node_g))

        for i in range(4):

            if i == 0 or i == 1:
                ng = move_vertical(node_g, i)
            else:
                ng = move_hori(node_g, i)
            vng = make_visit_ele(ng)

            if vng in visit:
                continue

            que.append((ng, cnt + 1))
            visit.add(vng)

    print(result)


def sol2():
    input = sys.stdin.readline

    n = int(input())
    g = list(list(map(int, input().split())) for _ in range(n))

    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

    def up(g):
        tmp_g = list(i[:] for i in g)

        for x in range(n):
            p = 0
            y = 1

            while y < n:

                if tmp_g[y][x] == 0:
                    y += 1
                    continue

                t = tmp_g[y][x]
                tmp_g[y][x] = 0

                if tmp_g[p][x] == 0:
                    tmp_g[p][x] = t

                elif tmp_g[p][x] == t:
                    tmp_g[p][x] *= 2
                    p += 1
                else:
                    p += 1
                    tmp_g[p][x] = t

                y += 1

        return tmp_g

    def down(g):
        tmp_g = list(i[:] for i in g)

        for x in range(n):
            p = n - 1
            y = n - 2

            while y >= 0:

                if tmp_g[y][x] == 0:
                    y -= 1
                    continue

                t = tmp_g[y][x]
                tmp_g[y][x] = 0

                if tmp_g[p][x] == 0:
                    tmp_g[p][x] = t

                elif tmp_g[p][x] == t:
                    tmp_g[p][x] *= 2
                    p -= 1

                else:
                    p -= 1
                    tmp_g[p][x] = t

                y -= 1

        return tmp_g

    def left(g):
        tmp_g = list(i[:] for i in g)

        for y in range(n):
            p = 0
            x = 1

            while x < n:

                if tmp_g[y][x] == 0:
                    x += 1
                    continue

                t = tmp_g[y][x]
                tmp_g[y][x] = 0

                if tmp_g[y][p] == 0:
                    tmp_g[y][p] = t
                elif tmp_g[y][p] == t:
                    tmp_g[y][p] *= 2
                    p += 1
                else:
                    p += 1
                    tmp_g[y][p] = t

                x += 1
        return tmp_g

    def right(g):
        tmp_g = list(i[:] for i in g)

        for y in range(n):
            p = n - 1
            x = n - 2

            while x >= 0:

                if tmp_g[y][x] == 0:
                    x -= 1
                    continue

                t = tmp_g[y][x]
                tmp_g[y][x] = 0

                if tmp_g[y][p] == 0:
                    tmp_g[y][p] = t

                elif tmp_g[y][p] == t:
                    tmp_g[y][p] *= 2
                    p -= 1
                else:
                    p -= 1
                    tmp_g[y][p] = t

                x -= 1

        return tmp_g

    def make_visit_ele(tmp_g):
        return tuple(tuple(i) for i in tmp_g)

    def cnt_max(tmp_g):
        return max(max(i) for i in tmp_g)

    que = deque()
    visit = set()

    tmp_g = list(i[:] for i in g)
    que.append((tmp_g, 0))
    visit.add(make_visit_ele(tmp_g))

    result = 0

    while que:

        node_g, cnt = que.popleft()

        if cnt > 5:
            break

        result = max(result, cnt_max(node_g))

        for i in range(4):

            if i == 0:
                ng = up(node_g)
            elif i == 1:
                ng = down(node_g)
            elif i == 2:
                ng = left(node_g)
            elif i == 3:
                ng = right(node_g)

            vng = make_visit_ele(ng)

            if vng in visit:
                continue

            # print(ng, cnt + 1, i)

            que.append((ng, cnt + 1))
            visit.add(vng)

    print(result)

