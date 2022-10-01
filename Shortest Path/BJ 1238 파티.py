import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline

n, m, x = map(int, input().split())
g = defaultdict(list)

for i in range(m):
    s,e,d = map(int, input().split())

    g[s].append((e,d))

#print(g)

answer = []

def bfs(start, end):

    que = []
    visited = [1e9] * (n + 1)

    heapq.heappush(que, [0, start])
    visited[start] = 0

    while que:

        d, node = heapq.heappop(que)

        if visited[node] < d:
            continue

        for i in g[node]:
            tnode, td = i
            new_d = td + d

            if visited[tnode] > new_d:
                visited[tnode] = new_d
                heapq.heappush(que, [new_d, tnode])

    return visited[end]


for i in range(1, n + 1):

    if i == x:
        continue

    t = 0
    t = (bfs(i,x)) + (bfs(x, i))
    answer.append(t)

print(max(answer))











