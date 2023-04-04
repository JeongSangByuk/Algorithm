import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

input = sys.stdin.readline

# N극 : 0, S극 : 1
# 시계 : 1, 반시계 : -1
g = list(list(map(int, input().strip())) for _ in range(4))
n = int(input())
command = list(map(int, input().split()) for _ in range(n))


def move(t1):
    k = t1.pop()
    t1.appendleft(k)
    return t1


def move_oppo(t2):
    k = t2.popleft()
    t2.append(k)
    return t2


def rotate(g, ro_tpye, i1, i2, k1, k2):
    t1 = deque(g[i1][:])
    t2 = deque(g[i2][:])

    is_rotated = False

    if g[i1][k1] != g[i2][k2]:

        is_rotated = True

        # 시계 방향 회전이면
        if ro_tpye == 1:
            t1 = move(t1)
            t2 = move_oppo(t2)
        else:
            t1 = move_oppo(t1)
            t2 = move(t2)
    else:
        if ro_tpye == 1:
            t1 = move(t1)
        else:
            t1 = move_oppo(t1)

    return list(t1), list(t2), is_rotated


def make_oppo_ro(ro):
    return 1 if ro == -1 else -1


for c in command:

    num, ro = c

    que = deque()
    que.append((num - 1, ro))

    visit = set()
    dic = dict()

    for i in range(4):
        dic[i] = g[i]

    while que:
        num, ro = que.popleft()

        if num == 0:
            t1, t2, is_rotated = rotate(g, ro, 0, 1, 2, 6)
            dic[0] = t1[:]

            if is_rotated and 1 not in visit:
                dic[1] = t2[:]
                que.append((1, make_oppo_ro(ro)))
                visit.add(1)

            visit.add(0)

        elif num == 1:

            t1, t2, is_rotated = rotate(g, ro, 1, 0, 6, 2)
            dic[1] = t1[:]

            if is_rotated and 0 not in visit:
                dic[0] = t2[:]
                que.append((0, make_oppo_ro(ro)))
                visit.add(0)

            t1, t2, is_rotated = rotate(g, ro, 1, 2, 2, 6)

            if is_rotated and 2 not in visit:
                dic[2] = t2[:]
                que.append((2, make_oppo_ro(ro)))
                visit.add(2)

            visit.add(1)


        elif num == 2:
            t1, t2, is_rotated = rotate(g, ro, 2, 1, 6, 2)
            dic[2] = t1[:]

            if is_rotated and 1 not in visit:
                dic[1] = t2[:]
                que.append((1, make_oppo_ro(ro)))
                visit.add(1)

            t1, t2, is_rotated = rotate(g, ro, 2, 3, 2, 6)
            if is_rotated and 3 not in visit:
                dic[3] = t2[:]
                visit.add(3)
                que.append((3, make_oppo_ro(ro)))

            visit.add(2)

        elif num == 3:
            t1, t2, is_rotated = rotate(g, ro, 3, 2, 6, 2)
            dic[3] = t1[:]

            if is_rotated and 2 not in visit:
                dic[2] = t2[:]
                que.append((2, make_oppo_ro(ro)))
                visit.add(2)

            visit.add(3)

    for i in dic.keys():
        g[i] = dic[i][:]
    # print(g)

# print(g)
ans = 0

ans += 0 if g[0][0] == 0 else 1
ans += 0 if g[1][0] == 0 else 2
ans += 0 if g[2][0] == 0 else 4
ans += 0 if g[3][0] == 0 else 8

print(ans)
