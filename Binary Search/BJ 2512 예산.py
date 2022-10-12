import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline

n = int(input())
g = list(map(int, input().split()))
m = int(input())

g.sort()

def search():

    start = 0
    end = g[-1]

    while start <= end:

        mid = (start + end) // 2

        tmp = 0
        for i in range(n):
            tmp += min(mid, g[i])

        print(start, end, tmp)

        if tmp <= m:
            start = mid + 1
        else:
            end = mid - 1

    return end

print(search())
















