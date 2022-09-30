import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())

dic = dict()

for i in range(v):
    dic[i + 1] = []

for i in range(e):
    u,vv,w = map(int, input().split())
    dic[u].append([vv, w])

INF = 1e9
visited = [INF] * (v + 1)

que = []

# 시작 스타트
heapq.heappush(que, (0, k))
visited[k] = 0

while que:

    dist, node = heapq.heappop(que)

    if visited[node] < dist:
        continue

    for i in dic[node]:
        #print(visited, i[0], i[1])

        new_w = i[1] + dist

        if visited[i[0]] > new_w:
            heapq.heappush(que, (new_w,i[0]))
            visited[i[0]] = new_w

for i in range(1,len(visited)):

    if visited[i] >= INF:
        print("INF")
    else:
        print(visited[i])











