import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
dic = defaultdict(list)
dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
g = list(list(0 for _ in range(n)) for _ in range(n))
c = []
for _ in range(n * n):
    l = list(map(int, input().split()))
    c.append(l[0])
    dic[l[0]] = l[1:5]


def count_empty(y, x):
    cnt = 0
    for i in range(4):

        ny = y + dy[i]
        nx = x + dx[i]

        if not (0 <= ny < n and 0 <= nx < n):
            continue

        if g[ny][nx] == 0:
            cnt += 1

    return cnt


def get_by_one(student):
    love_s = set(dic[student])

    result = dict()
    _max = 0

    for y in range(n):
        for x in range(n):

            if g[y][x] != 0:
                continue

            cnt = 0

            for i in range(4):

                ny = y + dy[i]
                nx = x + dx[i]

                if not (0 <= ny < n and 0 <= nx < n):
                    continue

                if g[ny][nx] in love_s:
                    cnt += 1

            if cnt == 0:
                continue

            _max = max(_max, cnt)

            result[(y, x)] = cnt

    ans = []
    for i in result:

        if _max == result[i]:
            ans.append((i))

    return ans


def get_by_two(l):
    _max = 0

    if len(l) == 0:
        l = []

        for i in range(n):
            for j in range(n):
                if g[i][j] == 0:
                    l.append((i,j))

    result = dict()

    for i in l:
        k = count_empty(i[0], i[1])
        _max = max(_max, k)
        result[(i[0], i[1])] = k

    ans = []
    for i in result:

        if _max == result[i]:
            ans.append((i))

    return ans

def get_by_three(ans):
    return sorted(ans, key=lambda x:(x[0],x[1]))[0]

for i in range(n * n):

    t = get_by_one(c[i])

    if len(t) == 1:
        ans = t[0]
        g[ans[0]][ans[1]] = c[i]
        continue

    t2 = get_by_two(t)
    if len(t2) == 1:
        ans = t2[0]
        g[ans[0]][ans[1]] = c[i]
        continue

    t3 = get_by_three(t2)
    g[t3[0]][t3[1]] = c[i]

ans = 0
for y in range(n):
    for x in range(n):

        cnt = 0
        for i in range(4):

            ny = y + dy[i]
            nx = x + dx[i]

            if not (0 <= ny < n and 0 <= nx < n):
                continue
            tmp_s = dic[g[y][x]]
            if g[ny][nx] in tmp_s:
                cnt += 1

        if cnt != 0:
            ans += (10 ** (cnt - 1))

print(ans)
