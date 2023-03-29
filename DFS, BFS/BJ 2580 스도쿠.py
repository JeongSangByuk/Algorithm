import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = 9
g = list(list(map(int, input().split())) for _ in range(n))
r, c, blank = [], [], []
rec = list(list(set() for _ in range(n // 3)) for _ in range(n // 3))

for i in range(n):
    r.append(set(g[i]))

for i in range(n):
    t = set()
    for j in range(n):
        t.add(g[j][i])
    c.append(t)

for i in range(n):
    for j in range(n):
        rec[i // 3][j // 3].add(g[i][j])

for i in range(n):
    for j in range(n):
        if g[i][j] == 0:
            blank.append((i, j))

l = len(blank)

def printg():
    for i in g:
        print(*i, sep=' ')

def add_visit(y, x, i):
    c[x].add(i)
    r[y].add(i)
    rec[y // 3][x // 3].add(i)

def remove_visit(y, x, i):
    c[x].remove(i)
    r[y].remove(i)
    rec[y // 3][x // 3].remove(i)

def check(i, y, x):
    return i not in c[x] and i not in r[y] and i not in rec[y // 3][x // 3]

def dfs(idx):

    if idx == l:
        printg()
        exit()

    for i in range(1, 10):
        y, x = blank[idx][0], blank[idx][1]

        if not check(i, y, x):
            continue

        add_visit(y, x, i)
        g[y][x] = i
        dfs(idx + 1)
        remove_visit(y, x, i)

dfs(0)