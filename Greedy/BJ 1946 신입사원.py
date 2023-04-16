import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

t = int(input())


def sol():
    n = int(input())
    g = list(list(map(int, input().split())) for _ in range(n))

    g.sort(key=lambda x: (x[0]))

    result = 1
    _min = g[0][1]

    # print(g)

    for i in range(1, n):

        if _min < g[i][1]:
            continue
        _min = min(_min, g[i][1])

        result += 1

    print(result)


for i in range(t):
    sol()
