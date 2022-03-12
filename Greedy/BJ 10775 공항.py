import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
p = int(input())
g = list(int(input()) for _ in range(p))
parent = [i for i in range(n + 1)]

def find(cur):
    if parent[cur] == cur:
        return cur

    parent[cur] = find(parent[cur])
    return parent[cur]

def union(a, b):
    a = find(a)
    b = find(b)
    parent[b] = a

answer = 0

print(parent)

for i in g:
    tmp = find(i)
    if tmp == 0:
        break
    answer += 1
    union(tmp - 1, tmp)

print(answer)