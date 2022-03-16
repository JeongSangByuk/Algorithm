import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]


for i in range(1, n):

    for j in range(len(g[i])):

        if j == 0:
            g[i][j] = g[i-1][j] + g[i][j]
        elif j == i:
            g[i][j] = g[i-1][j -1] + g[i][j]
        else:
            g[i][j] = max(g[i-1][j - 1], g[i-1][j ]) + g[i][j]

print(max(g[n-1]))