import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

input = sys.stdin.readline

# 위 아래 왼 오
dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

n, m, k = map(int, input().split())
g = list(list(map(int, input().split())) for _ in range(n))
shark = list(map(int, input().split()))
shark_pro = list(list() for _ in range(m + 1))
shark_now = dict()

# 0 : 상어 num, 1 : 유지시간
shark_g = list(list(list({"smell": 0, "shark": 0} for _ in range(n)) for _ in range(n)))

for i in range(1, m + 1):
    for j in range(4):
        tmp = list(map(int, input().split()))
        shark_pro[i].append(list(map(lambda x: x - 1, tmp)))

for i in range(1, m + 1):
    shark_now[i] = {"y": 0, "x": 0, "d": shark[i - 1] - 1}

for i in range(n):
    for j in range(n):

        if g[i][j] == 0:
            continue

        shark_g[i][j]["smell"] = k
        shark_g[i][j]["shark"] = g[i][j]
        shark_now[g[i][j]]["y"] = i
        shark_now[g[i][j]]["x"] = j


# 1. 아무 냄새 없는 곳
# 2. 자신의 냄새 있는 곳
# 가능한 칸이 여러개면 우선순위 순으로

def all_discount():
    for y in range(n):
        for x in range(n):

            if shark_g[y][x]["smell"] == 0:
                continue

            shark_g[y][x]["smell"] -= 1

            if shark_g[y][x]["smell"] == 0:
                shark_g[y][x]["shark"] = 0

def move_from_pro(tvisit, i, d, y, x):
    for s in shark_pro[i][d]:
        ny = y + dy[s]
        nx = x + dx[s]

        # 상어 이동
        if (ny, nx) in tvisit:
            return (ny, nx, y, x, i, s)


def play():
    ans = list()
    for i in range(1, m + 1):

        if i not in shark_now:
            continue

        y, x, d = shark_now[i]["y"], shark_now[i]["x"], shark_now[i]["d"]

        visit = set()

        for j in range(4):

            ny = y + dy[j]
            nx = x + dx[j]

            if not (0 <= ny < n and 0 <= nx < n):
                continue

            # 갈수 있는 곳 다 넣기
            visit.add((ny, nx))

        # 비어있는 곳
        tvisit = set()

        if len(visit) <= 0:
            continue

        for v in visit:
            if (shark_g[v[0]][v[1]]["smell"] == 0 and shark_g[v[0]][v[1]]["shark"] == 0):
                tvisit.add((v[0], v[1]))

        if len(tvisit) > 0:
            ans.append(move_from_pro(tvisit, i, d, y, x))
            continue

        # 자신이 있던 곳으로
        tvisit = set()

        for v in visit:
            if shark_g[v[0]][v[1]]["shark"] == i:
                tvisit.add((v[0], v[1]))

        ans.append(move_from_pro(tvisit, i, d, y, x))

    for a in ans:
        ny, nx, y, x, i, s = a

        if i not in shark_now:
            continue

        if shark_g[ny][nx]["shark"] < shark_g[y][x]["shark"] and shark_g[ny][nx]["shark"] != 0:
            shark_now.pop(shark_g[y][x]["shark"], None)
            continue

        shark_g[ny][nx]["smell"] = k + 1
        shark_g[ny][nx]["shark"] = i

        # shark 업데이트
        shark_now[i]["y"], shark_now[i]["x"], shark_now[i]["d"] = ny, nx, s

cnt = 0
while cnt < 1001:

    play()
    all_discount()
    cnt += 1

    if len(shark_now) == 1:
        break

print(-1 if cnt > 1000 else cnt)
