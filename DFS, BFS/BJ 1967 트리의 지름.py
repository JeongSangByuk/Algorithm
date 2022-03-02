import sys
import heapq
from collections import deque, defaultdict
import itertools

sys.setrecursionlimit(10**7)

input = sys.stdin.readline

k = int(input())

dic = []

for i in range(k + 1):
    dic.append([])

for i in range(k - 1):
    v1, v2,w = map(int, input().split())
    dic[v1].append((v2,w))
    dic[v2].append((v1, w))

# 가장 끝 노드를 찾는다.
def search_end(now,visited,w):

    global max_node

    visited.add(now)

    isEnd = True

    for i in dic[now]:

        if not i[0] in visited:
            isEnd = False
            search_end(i[0],visited,w + i[1])

    if isEnd and max_node[1] < w:
        max_node = (now,w)

max_node = (0,0)
visited = set()

# 끝 노드의 값중 가장 가중치가 큰 값을 저장
search_end(1,visited,0)
start = max_node[0]

max_node = (0,0)
visited = set()

# 가장 가중치가 큰 값에서 dfs 한번 더 돌린다.
search_end(start,visited,0)
print(max_node[1])






