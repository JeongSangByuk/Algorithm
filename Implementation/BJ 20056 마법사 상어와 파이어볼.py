import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

input = sys.stdin.readline

n, m, k = map(int, input().split())
ball = list(list(map(int, input().split())) for _ in range(m))

dy, dx = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

que = deque()

for b in ball:
    r, c, m, s, d = b
    que.append((r - 1, c - 1, m, s, d))

ans = []

now = 0


def all_even(i):
    for j in i:
        if j[4] % 2 != 0:
            return False

    return True


def all_odd(i):
    for j in i:
        if j[4] % 2 == 0:
            return False

    return True


def move(que):
    new_que = deque()

    while que:

        r, c, m, s, d = que.popleft()

        r, c = (r + dy[d] * s) % n, (c + dx[d] * s) % n

        # if not (0 <= r < n and 0 <= c < n):
        #     continue

        new_que.append((r, c, m, s, d))

    dic = defaultdict(list)

    for i in new_que:
        dic[(i[0], i[1])].append((i[0], i[1], i[2], i[3], i[4]))

    result_que = list()
    for i in dic:

        key = i
        i = dic[i]
        # print(i, dic[i], "qweqwe")

        if len(i) == 1:
            # print(dic[key])
            if dic[key][0][2] > 0:
                td = dic[key][0]
                result_que.append((td[0], td[1], td[2], td[3], td[4]))

        elif len(i) > 1:

            dm, ds = 0, 0
            # print(i)
            for j in i:
                dm += j[2]
                ds += j[3]

            nm, ns = math.floor(dm / 5), math.floor(ds / len(i))

            if nm <= 0:
                continue

            if all_even(i) or all_odd(i):
                ta = (0, 2, 4, 6)
            else:
                ta = (1, 3, 5, 7)

            for ttt in ta:
                result_que.append((key[0], key[1], nm, ns, ttt))

    return result_que

for i in range(k):

    que = move(deque(que))

# print(que)

ans = 0
for i in que:
    ans += i[2]

print(ans)
