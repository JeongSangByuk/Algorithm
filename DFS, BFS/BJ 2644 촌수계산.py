import sys
import heapq
from collections import deque, defaultdict
import itertools

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())

a1, a2 = map(int, input().split())

m = int(input())

dic = {}

for i in range(m):
    p1, p2 = map(int, input().split())

    if p1 in dic:
        dic[p1].append(p2)
    else:
        dic[p1] = [p2]

    if p2 in dic:
        dic[p2].append(p1)
    else:
        dic[p2] = [p1]

visited = set()
answer = -1

def bfs(start):

    if (not start in dic) or (not a2 in dic):
        return -1

    if start == a2:
        return 0

    que = deque()
    que.append([start,0])
    visited.add(start)

    while que:

        # 0 : node , 1 : cnt
        node, cnt = que.popleft()

        # 1촌 수 계산
        if node == a2:
            return cnt

        for i in dic[node]:

            if not i in visited:
                que.append([i,cnt + 1])
                visited.add(i)
    return -1

answer = bfs(a1)

print(answer)
