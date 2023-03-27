import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())

visit = []

def dfs(now, cnt):

    if cnt == m:
        print(*visit, sep=' ')
        return

    for i in range(1, n + 1):

        if i not in visit:
            visit.append(i)
            dfs(i, cnt + 1)
            visit.pop()


for i in range(1, n+1):
    visit.append(i)
    dfs(i, 1)
    visit.pop()