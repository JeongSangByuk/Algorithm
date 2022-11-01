import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

v, e = map(int, input().split())
start = int(input())
dic = defaultdict(list)

visited = [9e9] * (v + 1)

for i in range(e):
    a,b,c = list(map(int, input().split()))
    dic[a].append([b,c])

def bfs():
    que = []
    heapq.heappush(que, (0, start))
    visited[start] = 0

    while que:

        w, node = heapq.heappop(que)

        if visited[node] < w:
            continue

        for i in dic[node]:
            if w + i[1] < visited[i[0]]:
                visited[i[0]] = (w + i[1])
                heapq.heappush(que, (w + i[1], i[0]))

bfs()
print(visited)





