import sys
import heapq
from collections import deque, defaultdict
import itertools

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

k = int(input())

dic = {}

for i in range(k):
    dic[i + 1] = []

for i in range(k - 1):
    v1, v2,w = map(int, input().split())
    dic[v1].append((v2,w))
    dic[v2].append((v1, w))

l = list(itertools.combinations(list(dic.keys()),2))

answer = 0

#print(dic)

def dfs(now, end, visited, w):

    visited.add(now)

    for i in dic[now]:

        if i[0] not in visited:

            if i[0] == end:
                return w + i[1]

            visited.add(i[0])

            ans = dfs(i[0],end,visited,w + i[1])

            if ans > 0:
                return ans

    return 0

answer = []

for v in l:
    visited = set()
    #print(v[0],v[1],dfs(v[0],v[1],visited, 0))
    answer.append(dfs(v[0],v[1],visited, 0))

# visited = set()
# print(dfs(1,4,visited,0))

print(max(answer))





