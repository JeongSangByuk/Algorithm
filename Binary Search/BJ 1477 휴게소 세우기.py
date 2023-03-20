import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

input = sys.stdin.readline

n, m, l = map(int, input().split())
g = list(map(int, input().split())) + [l]
g.sort()

# print(g)

# 최소 거리를 x으로 둔다면 최대 몇개의 휴개소를 세울 수 있는가?

def check(mid):

    # [0, 82, 201, 411, 555, 622, 755, 800]
    prev = 0
    tg = set()

    for i in g:

        if i - prev > mid:

            tmp = ((i - prev)//mid)

            for j in range(1, tmp + 1):
                tg.add(prev + mid * j)

            tg.add(i)
            prev = i

    if l in tg:
        tg.remove(l)


    # print(tg)
    # print(len(tg))

    # 1  69   70 71   800
    # 800개  n + 1개 n개        1개
    # F         f   t   T

    return (n + m) >= len(tg)

lo = 0
hi = l + 1

while lo + 1 < hi:

    mid = (lo + hi) // 2

    if check(mid):
        hi = mid
    else:
        lo = mid

print(hi)







