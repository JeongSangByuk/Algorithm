import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())

visited = [1e9] * 100001
visited2 = [-1] * 100001

def bfs():
    que = deque()

    que.append((n, 0))
    visited[n] = 0
    visited2[n] = -1

    while que:
        #print(que)
        node, d = que.popleft()

        if visited[node] < d:
            continue

        if 0 <= node + 1 and node + 1 <= 100000 and visited[node + 1] > d + 1:
            visited[node + 1] = d + 1
            visited2[node + 1] = node
            que.append((node + 1, d + 1))

        if 0 <= node - 1 and node - 1 <= 100000 and visited[node - 1] > d + 1:
            visited[node - 1] = d + 1
            visited2[node - 1] = node
            que.append((node - 1, d + 1))

        if 0 <= node * 2 and node * 2 <= 100000 and visited[node * 2] > d + 1:
            visited[node * 2] = d + 1
            visited2[node * 2] = node
            que.append((node * 2, d + 1))
bfs()

print(visited[k])

now = k
a = []
while now != -1:
    a.append(now)
    now = visited2[now]

a.reverse()
print(*a , sep=" ")


