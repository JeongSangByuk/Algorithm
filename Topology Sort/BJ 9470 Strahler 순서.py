import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


ans = []
n = int(input())


def sol():

    global ans

    dic = defaultdict(list)

    k, m, p = map(int, input().split())

    # 진입차수, 최대레벨, 최대래밸개수
    indegree = list([0,0,0] for _ in range(m + 1))

    for i in range(p):
        a, b = map(int, input().split())
        dic[a].append(b)

        # 진입차수 ++
        indegree[b][0] += 1

    que = deque()

    for i in range(1, m + 1):

        # 진입차수가 0이라먄,
        if indegree[i][0] == 0:
            que.append(i)
            indegree[i][1] = 1

    while que:
        node = que.popleft()

        for i in dic[node]:

            # 진입 차수 -1
            indegree[i][0] -= 1

            # 최대 래밸이 이전 노드가 더 높다면 바꿔준다.
            if indegree[i][1] < indegree[node][1]:
                indegree[i][1] = indegree[node][1]
                indegree[i][2] = 1

            # 최대 래밸이 같다면, 최대래밸 수 +1
            elif indegree[i][1] == indegree[node][1]:
                indegree[i][2] += 1

            # 진입 차수가 0이라면 큐에 넣어준다.
            if indegree[i][0] == 0:

                # 최대 레벨의 개수가 2이상이면 최대 레벨을 올려준다.
                if indegree[i][2] > 1:
                    indegree[i][1] += 1

                que.append(i)

    ans.append((k, indegree[m][1]))

for i in range(n):
    sol()

for i in ans:
    print(i[0], i[1])













