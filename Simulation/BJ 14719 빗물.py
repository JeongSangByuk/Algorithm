import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

h, w = map(int, input().split())
p = list(map(int, input().split()))
g = [[0] * w for _ in range(h)]

for i in range(w):
    for j in range(p[i]):
        g[h - j - 1][i] = 1


ans = 0

def move(th):
    global ans

    now = g[th][0]
    tmp = []

    for i in range(1, w):
        if now == 1:
            if g[th][i] == 0:
                tmp.append(i)

            if g[th][i] == 1:
                ans += len(tmp)
                tmp.clear()
                now = 1

        elif now == 0:
            if g[th][i] == 1:
                now = 1


for i in range(h):
    move(i)

print(ans)

