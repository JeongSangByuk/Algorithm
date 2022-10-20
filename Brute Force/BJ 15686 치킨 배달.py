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
g = [list(map(int, input().split())) for _ in range(n)]

# 완전 탐색
def solve1():

    c = []
    dic = dict()

    # 치킨 찾기. 집 찾기.
    for i in range(n):
        for j in range(n):
            if g[i][j] == 2:
                c.append((i,j))
            elif g[i][j] == 1:
                dic[(i,j)] = 9e9

    choose = list(itertools.combinations(c,m))

    def count(r1, r2, c1, c2):
         return abs(r1 - r2) + abs(c1 - c2)

    def countR(y, x):

        for i in range(n):
            for j in range(n):

                if g[i][j] == 1:
                    dic[(i,j)] = min(dic[(i,j)], count(y, i, x, j))

    def init():
        for i in dic:
            dic[i] = 9e9

    ans = 9e9

    for i in choose:

        init()
        for j in range(m):
            countR(i[j][0], i[j][1])
            ans = min(ans, sum(list(dic.values())))

    print(ans)


c = []
dic = dict()

# 치킨 찾기. 집 찾기.
for i in range(n):
    for j in range(n):
        if g[i][j] == 2:
            c.append((i,j))
        elif g[i][j] == 1:
            dic[(i, j)] = 9e9

cl = len(c)
visited = set()

def init():
    for i in dic:
        dic[i] = 9e9

def count(r1, r2, c1, c2):
    return abs(r1 - r2) + abs(c1 - c2)


def countR(y, x):
    for i in range(n):
        for j in range(n):

            if g[i][j] == 1:
                dic[(i, j)] = min(dic[(i, j)], count(y, i, x, j))


ans = 9e9

def dfs(start, d):

    if d == m:
        global ans
        #print(visited)
        t = list(visited)

        for j in range(m):
            countR(t[j][0], t[j][1])
            ans = min(ans, sum(list(dic.values())))

        init()


    for i in range(start + 1, cl):

        visited.add(c[i])
        dfs(i, d + 1)
        visited.remove(c[i])

    return

for i in range(cl):

    visited.add(c[i])
    dfs(i, 1)
    visited.remove(c[i])

print(ans)
































