import copy
import sys
import math
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def bfs(g, info):
    answer = []

    que = deque()
    que.append((1, 0, 0, g[0]))

    while que:

        sheep, wolf, now, tmp_g = que.popleft()
        #print(now, tmp_g)
        isLastNode = True

        for i in tmp_g:

            if i == now:
                continue

            if wolf + info[i] >= sheep:
                continue

            isLastNode = False

            # 노드에서의 간선 복사
            t = g[i].copy()

            # 부모 노드에서 자신 빼고 복사
            for k in tmp_g:
                if k != i:
                    t.add(k)

            que.append((sheep + (1 if info[i] == 0 else 0), wolf + (1 if info[i] == 1 else 0), i, t))

        # 마지막 노드라면
        if isLastNode:
            answer.append((sheep, wolf))

    return (answer[-1][0])

def solution(info, edges):

    g = dict()

    answer = 0

    for i in range(len(info)):
        g[i] = set()

    for i in edges:
        g[i[0]].add(i[1])
        #g[i[1]].append(i[0])


    #print(g)
    answer = bfs(g,info)
    #print(answer)
    return answer


info = eval(input())
edges = eval(input())
solution(info, edges)



