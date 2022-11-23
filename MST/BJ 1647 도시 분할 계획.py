import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
edges = []

for i in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

def find(p, a):

    if p[a] != a:
        p[a] = find(p,p[a])
    return p[a]

def union(p, a, b):
    a = find(p,a)
    b = find(p,b)

    if a < b:
        p[b] = a
    else:
        p[a] = b

p = [ i for i in range(n + 1)]

answer = 0
_max = 0

for i in edges:
    c, a, b = i

    if find(p, a) != find(p, b):
        union(p, a, b)
        _max = max(_max, c)
        answer += c

# print(_max)
print(answer - _max)





