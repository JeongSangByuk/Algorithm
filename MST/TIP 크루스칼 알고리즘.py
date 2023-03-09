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

    # 가중치 기준으로 정렬하기 위해 가중치 앞으로
    edges.append((c,a,b))

# 가중치 기준 정렬
edges.sort()

# 부모 리스트 초기화
parent =list(i for i in range(v + 1))

def find(x):

    # 부모의 값이 다르다면 한번더 find
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(a, b):

    # 각 정점의 부모 찾기
    a = find(parent, a)
    b = find(parent, b)

    # 더 작은 정점의 방향으로
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

result = 0

for i in edges:
    c, a, b = i

    # 각 정점에 부모가 다르다면 union
    if find(parent, a) != find(parent,b):
        union(parent,a,b)
        result += c

# print(parent)
print(result)














