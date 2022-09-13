import copy
import sys
import math
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())

g = list(map(int, input().split()))
l = len(g)

tmp_g = [0] * (l + 1)


for i in range(m):
    a,b,c = map(int, input().split())
    tmp_g[a - 1] += c
    tmp_g[b] -= c

for i in range(l):
    tmp_g[i + 1] += tmp_g[i]

for j in range(l):
    g[j] += tmp_g[j]

print(*g, sep= ' ')
#print(g)



