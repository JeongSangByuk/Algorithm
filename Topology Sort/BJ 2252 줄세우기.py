import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())

dic = defaultdict(list)

# 진입 차수
v = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    dic[a].append(b)
    v[b] += 1

ans = []
que = deque()

# 진입 차수 0일 때 append
for i in range(1, n + 1):
    if v[i] == 0:
        que.append(i)

while que:

    node = que.popleft()
    ans.append(node)

    for i in dic[node]:

        # 진입 차수 -1
        v[i] -= 1

        if v[i] == 0:
            que.append(i)

print(*ans, sep=' ')























