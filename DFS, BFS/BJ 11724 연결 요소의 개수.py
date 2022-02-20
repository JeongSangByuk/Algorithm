import sys
import heapq
from collections import deque, defaultdict
import itertools

input = sys.stdin.readline

# n 정점 개수, m 간선 개수
n, m = map(int, input().split())

dic = {}
visited = {}

# 간선 추가
for i in range(m):

    t1, t2 = map(int, input().split())

    if t1 in dic:
        dic[t1].append(t2)
    else:
        dic[t1] = [t2]
        visited[t1] = False

    if t2 in dic:
        dic[t2].append(t1)
    else:
        dic[t2] = [t1]
        visited[t2] = False

def bfs(start):

    que = deque()

    que.append(start)
    visited[start] = True

    while que:

        node = que.popleft()

        for t in dic[node]:

            if not visited[t]:
                visited[t] = True
                que.append(t)

cnt = 0

for t in dic:

    if not visited[t] :
        bfs(t)
        cnt += 1

cnt_visited = 0
for t in visited:
    if visited[t]:
        cnt_visited += 1

if m == 0:
    print(n)
else:
    print(cnt + n - cnt_visited)

