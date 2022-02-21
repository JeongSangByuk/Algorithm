import sys
import heapq
from collections import deque, defaultdict
import itertools

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())

dic = {}

arr = [0] * n

visited = set()

for i in range(n - 1):
    p1, p2 = map(int, input().split())

    if p1 in dic:
        dic[p1].append(p2)
    else:
        dic[p1] = [p2]

    if p2 in dic:
        dic[p2].append(p1)
    else:
        dic[p2] = [p1]

def dfs(start):

    for node in dic[start]:
        if not node in visited:
            #print(node)
            arr[node - 1] = start
            visited.add(node)
            dfs(node)

visited.add(1)
dfs(1)

for i in range(1,n):
    print(arr[i])

