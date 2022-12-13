import math
import sys
from collections import deque
import itertools
import heapq
from bisect import bisect_left

# sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def sol():
    k = 10000000

    l = int(input())
    n = int(input())
    g = list(int(input()) for _ in range(n))

    g.sort()

    i, j = 0, n - 1
    s = l * k
    while i < j:

        if g[i] + g[j] == l * k:
            print("yes", g[i], g[j])
            return
        elif g[i] + g[j] > s:
            j -= 1
        elif g[i] + g[j] < s:
            i += 1

    print("danger")

while True:

    try:
        sol()

    except:
        break
