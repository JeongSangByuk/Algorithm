import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

# sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


n = int(input())
m = int(input())

dic = defaultdict(list)

for i in range(m):
    a,b,c = map(int, input().split())
    dic[a].append((b,c))

start, end = map(int, input().split())

def bfs(start, end):

    que = []
    heapq.heappush(que, (0, start))

    v = [9e9 for _ in range(n + 1)]
    v[start] = 0

    while que:

        d, now = heapq.heappop(que)

        if v[now] < d:
            continue

        for i in dic[now]:

            _next, _d = i
            cost = d + _d

            if cost < v[_next]:
                v[_next] = cost
                heapq.heappush(que, (cost, _next))

    return v[end]

print(bfs(start,end))



