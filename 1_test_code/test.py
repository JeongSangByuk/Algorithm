import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

# https://blog.naver.com/jinhan814/222607789392

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

k = 3
g = [1, 2, 3, 3, 3, 4]
g.sort()

print(g)


# check(lo) != check(hi) 되도록 lo, hi를 설정하자.
# 중요한 것은, check(lo) != check(hi) 인 시점이 답.
# TF or FT 구간을 발견할 수 있게끔 결정함수를 만들자.
# 결국 정답을 구할 수 있게끔 결정함수를 잘 만들어야 한다!!

# 결정 함수가 TF 분포
#   결정함수 True, lo = mid

# 결정 함수가 FT 분포
#   결정함수 True, hi = mid

def bs_lower_bound_FT():
    def check_lower_FT(mid):
        # 처음으로 g[mid]가 k보다 크거나 같아지는 시점을 찾는다
        # 1,2,3,3,3,4 -> F,F,T,T,T,T 가 되도록 check 함수 짜기
        # 이때 FT 분포이기때문에 hi return
        return g[mid] >= k

    # 값이 아니라 인덱스의 개념, 매개변수탐색과의 차이.
    lo = -1
    hi = len(g)

    while lo + 1 < hi:

        mid = (lo + hi) // 2

        if check_lower_FT(mid):
            hi = mid
        else:
            lo = mid

    return hi


def bs_lower_bound_TF():

    def check_lower_TF(mid):

        # 1,2,3,3,3,4 -> T,T,F,F,F,F 가 되도록 check 함수 짜기
        return g[mid] < k

    lo = -1
    hi = len(g)

    while lo + 1 < hi:

        mid = (lo + hi) // 2

        if check_lower_TF(mid):
            lo = mid
        else:
            hi = mid

    return hi


def bs_upper_bound_FT():

    def check_upper_FT(mid):
        # 다시 한번, check 함수의 목적은 TF or FT가 갈리는 시점을 찾는 것이다!
        # 그것을 기준으로 check 함수를 만든다.
        # F,F,F,F,F,T
        # 처음으로  g[mid]가 k보다 커지는 시점을 찾는다
        return g[mid] > k

    lo = 0
    hi = len(g)

    while lo + 1 < hi:

        mid = (lo + hi) // 2

        if check_upper_FT(mid):
            hi = mid
        else:
            lo = mid

    return lo


def bs_upper_bound_TF():

    def check_upper_TF(mid):

        # 1,2,3,3,3,4 -> T,T,T,T,T,F 가 되도록 check 함수 짜기
        return g[mid] <= k

    lo = 0
    hi = len(g)

    while lo + 1 < hi:

        mid = (lo + hi) // 2

        if check_upper_TF(mid):
            lo = mid
        else:
            hi = mid

    return lo


print(bs_lower_bound_FT())
print(bs_lower_bound_TF())
print(bs_upper_bound_FT())
print(bs_upper_bound_TF())

