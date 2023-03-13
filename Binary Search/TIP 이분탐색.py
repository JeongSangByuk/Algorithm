import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


n = 1000

left = 0
right = n

# lower_bound : 탐색 값 중 가장 작은 값을 인덱스를 반환
def bs_lower_bound(k):

    while (left <= right):
        mid = (left + right) // 2

        if mid < k:
            left = mid + 1
        else:
            right = mid - 1

    return left

# lower_bound : 탐색 값 중 가장 큰 값을 인덱스를 반환
def bs_upper_bound(k):

    while(left <= right):
        mid = (left + right) // 2

        if mid <= k:
            left = mid + 1
        else:
            right = mid - 1

    return right







