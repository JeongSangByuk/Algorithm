import sys
from collections import deque
import itertools

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
g = list(map(int, input().split()))
m = int(input())

dic = {}
start = 0

for i in range(len(g)):

    if g[i] == -1:
        start = i
        continue

    if g[i] in dic:
        dic[g[i]].append(i)
    else:
        dic[g[i]] = [i]

visited = set()
removed = []

def search_removed_node(n):

    removed.append(n)

    if not n in dic:
        return

    for i in dic[n]:
        if not i in visited:
            visited.add(i)
            search_removed_node(i)

def search_leaf(n):

    global answer
    cnt = 0

    if n in dic and len(dic[n]) != 0:

        for i in dic[n]:
            if not i in visited:
                cnt += 1
                visited.add(i)
                search_leaf(i)

    if cnt == 0:
        answer += 1

# 삭제할 노드 찾고, 삭제
search_removed_node(m)

for i in dic:
    for j in removed:
        if j in dic[i]:
            dic[i].remove(j)

visited.clear()

answer =0

# leaf 노드 찾기
search_leaf(start)

# 루트 노드 삭제시 0 출력
if m == start:
    print(0)
else:
    print(answer)