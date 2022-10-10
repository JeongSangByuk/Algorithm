import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
g = list(map(int, input().split()))
g.sort()

def search():
    start = 1
    end = g[n-1]

    while start <= end:

        mid = (start + end) // 2

        tmp = 0

        # 나무 계산
        for i in range(n):
            if g[i] > mid:
                tmp += (g[i] - mid)

        if tmp >= m:
            start = mid + 1
        else:
            end = mid - 1

    return end

print(search())







