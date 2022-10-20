import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)

n = int(input())
g = list(int(input()) for i in range(n))
dic = defaultdict(int)

for i, k in enumerate(g):
    dic[i + 1] = k

visited = set()

def dfs(start):
    global visited

    a = dic[start]

    visited.add(start)
    if dic[start] not in visited:
        a = dfs(dic[start])
    # visited.remove(start)

    return a

answer = set()

for i in range(1, n + 1):

    visited.clear()
    d = dfs(i)

    if i == d:

        answer.update(visited.copy())

l = list(answer)
l.sort()

print(len(l))
print(*l, sep='\n')












