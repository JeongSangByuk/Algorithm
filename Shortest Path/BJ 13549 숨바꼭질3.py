import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())

visited = [1e9] * 100003

def bfs():
    que = deque()

    que.append((n, 0))
    visited[n] = 0

    while que:
        #print(que)
        node, d = que.popleft()

        if visited[node] < d:
            continue

        if 0 <= node + 1 and node + 1 <= 100000 and visited[node + 1] > d + 1:
            visited[node + 1] = d + 1
            que.append((node + 1, d + 1))

        if 0 <= node - 1 and node - 1 <= 100000 and visited[node - 1] > d + 1:
            visited[node - 1] = d + 1
            que.append((node - 1, d + 1))

        if 0 <= node * 2 and node * 2 <= 100000 and visited[node * 2] > d:
            visited[node * 2] = d
            que.append((node * 2, d))
bfs()
print(visited[k])