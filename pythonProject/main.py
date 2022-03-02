import sys
import heapq
from collections import deque, defaultdict
import itertools

sys.setrecursionlimit(10**7)

input = sys.stdin.readline

n, k = map(int, input().split())


que = deque()
que.append((n,0))
visited = set()
visited.add(n)

while que:

    #print(que)
    node = que.popleft()

    if node[0] == k:
        print(node[1])
        break

    elif node[0] < 0:
        continue

    elif node[0] > 200000:
        continue

    if (node[0] - 1) not in visited:
        que.append((node[0] - 1, node[1] + 1))
        visited.add((node[0] - 1))

    if (node[0] + 1) not in visited:
        que.append((node[0] + 1, node[1] + 1))
        visited.add((node[0] + 1))

    if (node[0] * 2) not in visited:
        if node[0] * 2 <= k + 1:
            que.append((node[0] * 2, node[1] + 1))
            visited.add((node[0] * 2))
