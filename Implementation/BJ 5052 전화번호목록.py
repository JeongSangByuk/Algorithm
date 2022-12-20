import math
import sys
from collections import deque
import itertools
import heapq
from bisect import bisect_left

# sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

t = int(input())

def sol():

    n = int(input())
    g = list(input().strip() for _ in range(n))
    g.sort()

    g = list(map(str, g))
    print(g)

    for i in range(n - 1):
        l = len(g[i])
        if g[i] == g[i + 1][:l]:
            return False

    return True

for _ in range(t):
    if sol():
        print("YES")
    else:
        print("NO")
























