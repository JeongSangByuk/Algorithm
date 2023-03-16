import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

# 참고 : https://seongonion.tistory.com/100

n = int(input())
g = list(map(int,input().split()))

def sol1_binary_search():

    def make_tmp(i, current):
        return current + liquids[i]

    def check(mid, current):
        tmp = make_tmp(mid, current)

        # 음수에서 양수로 넘어가는 부분이 가장 절대값이 작을 것이다.
        # -101 -99 -2 -1 4 98 103
        #      -200 -102 -102 -97 -3 2
        #       T   T    T    T   T  F
        #
        # 찾고 싶은 부분은? tmp < 0 인가?

        return tmp < 0

    for i in range(n - 1):
        current = liquids[i]

        lo = i + 1
        hi = n - 1

        while lo + 1 < hi:
            mid = (lo + hi) // 2

            if check(mid, current):
                lo = mid
            else:
                hi = mid

        tmp_ans = ans
        tmp_ans_index = (ans_index[0], ans_index[1])

        if abs(make_tmp(lo, current)) < abs(make_tmp(hi, current)):
            tmp_ans = abs(make_tmp(lo, current))
            tmp_ans_index = (i, lo)
        else:
            tmp_ans = abs(make_tmp(hi, current))
            tmp_ans_index = (i, hi)

        if abs(tmp_ans) < ans:
            ans = tmp_ans
            ans_index = tmp_ans_index

    print(liquids[ans_index[0]], liquids[ans_index[1]])

def sol2_two_pointer():
    start = 0
    end = n - 1
    m = 2e9
    a1, a2 = 0, 0

    while start < end:

        s = g[start] + g[end]

        if abs(s) < m:
            m = abs(s)
            a1, a2 = g[start], g[end]

        if s < 0:
            start += 1
        else:
            end -= 1

    print(a1, a2)





























