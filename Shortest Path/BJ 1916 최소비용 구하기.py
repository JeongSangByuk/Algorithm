import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline

city = int(input())
bus = int(input())
g = defaultdict(list)

for i in range(bus):
    a, b, c = map(int, input().split())
    g[a].append((b, c))

start, end = map(int, input().split())

visited = [1e9] * (city + 1)


def bfs():
    que = []
    heapq.heappush(que, (0, start))
    visited[start] = 0

    while que:
        w, node = heapq.heappop(que)

        if visited[node] < w:
            continue

        for n in g[node]:
            nc, nw = n
            if (nw + w) < visited[nc]:
                visited[nc] = (nw + w)
                heapq.heappush(que, (nw + w, nc))

bfs()
print(visited)
print(visited[end])