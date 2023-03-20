import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

input = sys.stdin.readline

n, atk = map(int, input().split())
g = list()
for i in range(n):
    # type a h
    # t == 1, 공격력a, 피h인 몬스터
    # t == 2, 공격력a 상승, 피h 상승 포션
    g.append(tuple(map(int, input().split())))

# print(g)


# 최대 생명력이 mid일때 이길 수 있는가??

def check(mid):
    now_h = mid
    now_a = atk

    for i in g:

        t, a, h = i

        if t == 1:

            # 용사가 몬스터를 물리치기위해 공격해야하는 횟수
            acnt = math.ceil(h/now_a)

            # 위의 횟수동안 몬스터가 공격할 수 있는 데미지
            md = (acnt-1) * a

            if now_h - md <= 0:
                return False
            else:
                now_h -= md

        elif t == 2:
            now_a += a

            now_h += h

            if now_h > mid:
                now_h = mid

    # 1         49    50      9e9
    # false     false true        true
    return True

lo,hi = 0, n * 1000000 * 1000000 + 1

while lo + 1 < hi:

    # print(lo, hi)
    mid = (lo + hi) // 2

    if check(mid):
        hi = mid
    else:
        lo = mid
print(hi)
