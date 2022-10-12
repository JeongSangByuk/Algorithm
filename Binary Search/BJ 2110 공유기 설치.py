import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline

n, c= map(int, input().split())

g = [int(input()) for _ in range(n)]

g.sort()

def search():

    start = 1
    end = g[-1] - g[0]

    while start <= end:
        mid = (start + end) // 2

        tmp = 1
        prev = g[0]

        for i in range(1, n):

            if g[i] >= prev + mid:
                tmp += 1
                prev = g[i]

        if tmp >= c:
            start = mid + 1
        else:
            end = mid - 1

    return end

print(search())











