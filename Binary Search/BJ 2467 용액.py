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
    ans = 9e9
    ans_yx = (0,0)

    for i in range(n - 1):

        now = g[i]

        l = i + 1
        r = n - 1
        print(g[l:r + 1])

        while l <= r:
            mid = (l + r)//2
            tmp = now + g[mid]

            if abs(tmp) < ans:
                ans = abs(tmp)
                ans_yx = (i, mid)

                if tmp == 0:
                    break

            # 이진탐색과 투포인터를 활용
            # 합의 절대값이 0보다 작으면 양수가 되게끔,
            if tmp < 0:
                l = mid + 1
            else:
                r = mid - 1

    print(g[ans_yx[0]], g[ans_yx[1]])

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





























