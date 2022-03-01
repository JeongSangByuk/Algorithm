import sys
import heapq
from collections import deque, defaultdict
import itertools

sys.setrecursionlimit(100000)

input = sys.stdin.readline

k = int(input())

def dfs(now, dic,visited, num):

    visited[now - 1] = num

    next_num = 0

    if num == 1:
        next_num = -1
    else:
        next_num = 1

    for i in dic[now]:

        # 이분할 조건에 안맞을 경우
        if visited[i - 1] == num:
            return "NO"

        # 방문하지 않은 노드에 대해서는 dfs
        if visited[i - 1] == 0:
            ans = dfs(i,dic,visited, next_num)

            if ans == "NO":
                return "NO"

    return "YES"

answer = []

for i in range(k):

    v,e = map(int, input().split())

    dic = {}
    visited = [0 for _ in range(v)]

    for j in range(v):
        dic[j + 1] = []

    for j in range(e):
        v1, v2 = map(int, input().split())

        dic[v1].append(v2)
        dic[v2].append(v1)

    # 정점 하나씩 돌면서 dfs
    for j in range(v):
        if visited[j] == 0 :
            ans = dfs(j + 1,dic,visited,1)

            if ans == "NO":
                answer.append(ans)
                break

    if len(answer) == i:
        answer.append("YES")

for i in answer:
    print(i)


