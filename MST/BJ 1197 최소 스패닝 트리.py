import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

v, e = map(int, map(int, input().split()))

edges = []

for i in range(e):
    a,b,c = map(int, input().split())
    edges.append((c,a,b))

edges.sort()

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent =list(i for i in range(v + 1))

result = 0

for i in range(e):
    c, a, b = edges[i]

    if find(parent, a) != find(parent,b):
        union(parent,a,b)
        result += c

# print(parent)
print(result)














