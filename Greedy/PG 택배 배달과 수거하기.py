import math
import sys
from collections import deque
from collections import defaultdict
import itertools
from heapq import heappop, heappush
from bisect import bisect_left

def solution2(cap, n, deliveries, pickups):
    answer = 0

    # 역순으로 누적합
    for i in range(n-2, -1, -1):
        deliveries[i] += deliveries[i+1]
        pickups[i] += pickups[i+1]
    k = 0

    for i in range(n-1, -1, -1):
        while deliveries[i] > cap*k or pickups[i] > cap*k:
            answer += (i+1)*2
            k += 1
    return answer


def solution(cap, n, deliveries, pickups):

    # https://americanoisice.tistory.com/198

    answer = 0
    need_d, need_p = 0, 0

    # 1 0 3 1 2
    # 0 3 0 4 0

    # 2, 0
    # -2, -4
    # -1, 0
    #  2, 0
    # -2, -4
    # -2, -1
    # -1, -1

    for i in range(n - 1, -1, -1):

        need_d += deliveries[i]
        need_p += pickups[i]

        while need_d > 0 or need_p > 0:
            need_d -= cap
            need_p -= cap
            answer += (i + 1) * 2

    return answer
















