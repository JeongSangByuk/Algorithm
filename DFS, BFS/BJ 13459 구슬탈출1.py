import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())
g = list(list(input().strip()) for _ in range(n))
print(g)
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

init_b, init_r = (0, 0), (0, 0)

for i in range(n):
    for j in range(n):
        if g[i][j] == 'R':
            init_r = (i, j)
            g[i][j] = "."
        elif g[i][j] == 'B':
            init_b = (i, j)
            g[i][j] = "."

print(g)
def move(now_p, tp):
    cnt = 0
    y, x = now_p[0], now_p[1]

    while True:

        ny = y + dy[tp]
        nx = x + dx[tp]

        if 0 <= ny < n and 0 <= nx < m and g[ny][nx] != '#':

            cnt += 1

            # 골인일 경우 return
            if g[ny][nx] == "O":
                return ((-100, -100), cnt)

            y, x = ny, nx

        else:
            return ((y, x), cnt)



def bfs():
    que = deque()
    que.append((init_b, init_r, 0))

    visit = set()
    visit.add((init_b, init_r))
    print(que)
    print(g)

    while que:
        now_b, now_r, cnt = que.popleft()

        if cnt >= 10:
            return 0

        for i in range(4):

            moved_b, b_cnt = move(now_b, i)
            moved_r, r_cnt = move(now_r, i)

            print(moved_b, moved_r)

            # 둘다 들감
            if moved_b == (-100, -100):
                continue

            elif moved_r == (-100, -100):
                return 1

            # 위치가 같다면 조금
            if moved_r == moved_b:

                if b_cnt < r_cnt:
                    moved_r = (moved_r[0] - dy[i], moved_r[1] - dx[i])

                else:
                    moved_b = (moved_b[0] - dy[i], moved_b[1] - dx[i])

            if (moved_b, moved_r) not in visit:
                que.append((moved_b, moved_r, cnt + 1))
                visit.add((moved_b, moved_r))

    return 0


print(bfs())
