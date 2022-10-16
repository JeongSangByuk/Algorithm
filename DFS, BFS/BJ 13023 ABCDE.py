import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

g = defaultdict(list)

for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited = set()

def dfs(node,cnt):

    if cnt == 4:
        print(1)
        exit()

    for i in g[node]:

        if i not in visited:

            visited.add(i)
            dfs(i, cnt + 1)
            visited.remove(i)

    return False


for i in range(n):

    visited.add(i)
    dfs(i,0)
    visited.remove(i)

print(0)



















