import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

t = int(input())
result = []

# 해당하는 네트워크만 찾기 위해
def bfs(start, dic):

    que = deque()
    visited = set()
    que.append(start)
    visited.add(start)

    while que:

        node = que.popleft()

        for i in dic[node]:

            if i not in visited:
                que.append(i)
                visited.add(i)

    return list(visited)

def sol():

    global result

    n, m = map(int, input().split())
    time = [0] + list(map(int, input().split()))

    dic = defaultdict(list)
    dic_reverse = defaultdict(list)

    v = [0] * (n + 1)
    v_time = [0] * (n + 1)

    for i in range(m):
        a, b = map(int, input().split())
        dic[a].append(b)
        dic_reverse[b].append(a)
        v[b] += 1

    w = int(input())
    que = deque()

    # 다른 네트워크에 있는 노드를 제외하기 위함.
    s = bfs(w, dic_reverse)

    for i, k in enumerate(v):

        # 진입 차수가 0 이고, 해당하는 네트워크에서만 시작하기 위해
        if k == 0 and i in s:

            if i == w:
                result.append(time[i])
                return

            # 시작점 add
            que.append((i, time[i]))
            v_time[i] = time[i]

    while que:

        node, time_sum = que.popleft()

        for i in dic[node]:

            v[i] -= 1
            v_time[i] = max(v_time[i], time_sum + time[i])

            if v[i] == 0:
                que.append((i, v_time[i]))

    result.append(v_time[w])

for i in range(t):
    sol()

print(*result, sep="\n")




























