import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline

n, e = map(int, input().split())
g = defaultdict(list)

for i in range(e):
    a, b, w = map(int, input().split())
    g[a].append([b,w])
    g[b].append([a,w])

u, v = map(int, input().split())

#print(g)
def bfs(start, end):

    que = []
    heapq.heappush(que, [0,start])
    visited = [1e9] * (n + 1)
    visited[start] = 0

    while que:

        d, node = heapq.heappop(que)

        if visited[node] < d:
            continue

        for i in g[node]:
            tnode, dt = i
            new_d = d + dt

            if new_d < visited[tnode]:
                visited[tnode] = new_d
                heapq.heappush(que, [new_d, tnode])

    #print(visited)
    return visited[end]


a,b,c = bfs(1,u), bfs(u,v), bfs(v, n)
aa,bb,cc = bfs(1,v), bfs(v,u), bfs(u, n)

a1, a2 = 0,0

if a >= 1e9 or b >= 1e9 or c >= 1e9:
    a1 = 1e9
else:
    a1 = sum((a,b,c))

if aa >= 1e9 or bb >= 1e9 or cc >= 1e9:
    a2 = 1e9
else:
    a2 = sum((aa,bb,cc))

if a1 >= 1e9 and a2 >= 1e9:
    print(-1)
else:
    print(min(a1,a2))












