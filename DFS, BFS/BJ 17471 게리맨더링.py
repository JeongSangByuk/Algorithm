import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
g = list(map(int, input().split()))
dic = defaultdict(set)

for i in range(n):
    t = list(map(int, input().split()))

    for j in range(1, len(t)):
        dic[i + 1].add(t[j])

ar = set()

for k in range(1, n // 2 + 1):
    cnt = 0
    it = list(itertools.combinations([i for i in range(1, n + 1)], k))

    for i in it:
        base = set(j for j in range(1, n + 1)).difference(set(i))
        t = tuple((i, tuple(base)))
        ar.add(t)


def bfs(tg):
    start = tg[0]

    que = deque()
    visit = set()
    tg = set(tg)

    que.append(start)
    visit.add(start)

    while que:

        node = que.popleft()

        for i in dic[node]:
            if i not in visit and i in tg:
                que.append(i)
                visit.add(i)

    return len(tg) == len(visit)


result = 9e9

for i in ar:
    if bfs(i[0]) and bfs(i[1]):
        a = sum(list(g[j - 1] for j in i[0]))
        b = sum(list(g[j - 1] for j in i[1]))

        result = min(result, abs(a - b))

print(result if result != 9e9 else -1)
