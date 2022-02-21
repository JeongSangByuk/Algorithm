import sys
import heapq
from collections import deque, defaultdict
import itertools

input = sys.stdin.readline

n, m, v = map(int, input().split())
dic = {}

for i in range(m):
    t1, t2 = map(int, input().split())

    if t1 in dic:
        dic[t1].append(t2)
    else:
        dic[t1] = [t2]

    if t2 in dic:
        dic[t2].append(t1)
    else:
        dic[t2] = [t1]

for i in dic:
    dic[i].sort()

def dfs(start):

    stack = deque()
    stack.append(start)
    visit = []

    while stack:

        node = stack.pop()

        if node not in visit:
            visit.append(node)

            for i in reversed(dic[node]) :
                    stack.append(i)

    visit = map(str,visit)
    print(' '.join(visit))


visited = []

def dfs2(start):

    visited.append(start)

    for node in dic[start]:
        if node not in visited:
            print(node)
            dfs2(node)


def bfs(start):

    que = deque()
    que.append(start)
    visit = [start]

    while que :

        node = que.popleft()

        for i in dic[node]:

            if i not in visit:

                visit.append(i)
                que.append(i)

    visit = map(str,visit)
    print(' '.join(visit))

dfs2(v)
#bfs(v)





