import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())

v = []
dic = dict()
edges = []

for i in range(n):
    a, b = map(float, input().split())
    v.append((a, b))
    dic[(a,b)] = i + 1

for i in range(len(v)):
    for j in range(i + 1, len(v)):

        c = math.sqrt((v[i][0] - v[j][0]) * (v[i][0] - v[j][0]) + (v[i][1] - v[j][1]) * (v[i][1] - v[j][1]))
        edges.append((round(c, 2), dic[v[i]], dic[v[j]]))

def find(p, a):

    if p[a] != a:
        p[a] = find(p,p[a])
    return p[a]

def union(p, a, b):

    a = find(p, a)
    b = find(p, b)

    if a < b:
        p[b] = a
    else:
        p[a] = b

edges.sort()
p = [ i for i in range(n + 1)]

answer = 0

for i in edges:

    c, a, b = i
    if find(p, a) != find(p, b):
        union(p,a,b)
        answer += c

# print(edges)
print(answer)



