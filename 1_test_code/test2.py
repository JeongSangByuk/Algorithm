import sys
from collections import deque
import itertools

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())

dic = {}
v = {}

for i in range(1, n):

    t1, t2, w = map(int, input().split())

    if t1 in dic:
        dic[t1].append((t2,w))
    else:
        dic[t1] = [(t2,w)]

    if t2 in dic:
        dic[t2].append((t1,w))
    else:
        dic[t2] = [(t1,w)]

for i in range(1, n):

    t1, t2 = map(int, input().split())

    v[t1] = t2

answer_visited = set()
visited = set()

# print(dic)
# print(v)

answer = [(0,0)]

def dfs(now, nowPass):

    global answer

    visited.add(now)

    for i in dic[now]:

        if not i[0] in visited:

            tmpMoney = 0
            nowPass += i[0]

            if i[0] in v:
                tmpMoney = v[i[0]] - (nowPass * 2)

            if not i[0] in answer_visited and answer[0][1] < tmpMoney:
                answer.clear()
                answer.append((i[0], tmpMoney))
            elif not i[0] in answer_visited and answer[0][1] == tmpMoney:
                answer.append((i[0], tmpMoney))

            dfs(i[0], nowPass)

dfs(1, 0)

answer.sort(key= lambda x : x[1])
print(answer[0][1],answer[0][0])