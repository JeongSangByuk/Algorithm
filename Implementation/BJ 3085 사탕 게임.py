import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
g = [list(input().strip()) for _ in range(n)]
dy,dx = [1,0],[0,1]

ans = 0
def dfs(y, x, now, i, cnt,tg):

    t = cnt

    # 같은 색인 경우에만 진행
    if y + dy[i] < n and x + dx[i] < n and now == tg[y + dy[i]][x + dx[i]]\
            and (y + dy[i], x + dx[i]) not in visited:
        visited.add((y + dy[i], x + dx[i]))
        t = dfs(y + dy[i], x + dx[i], now, i, cnt + 1, tg)
    #print(cnt, t)
    return t

visited = set()

def move(k,tg):

    global ans

    visited.clear()
    for i in range(n):
        for j in range(n):

            if (i,j) not in visited:
                visited.add((i,j))
                ans = max(ans ,dfs(i,j,tg[i][j], k, 1, tg))


def change(y1,x1, y2,x2):

    global ans

    if g[y1][x1] == g[y2][x2]:
        return

    tg = [t[:] for t in g]

    # swap
    c = tg[y1][x1]
    tg[y1][x1] = tg[y2][x2]
    tg[y2][x2] = c

    for i in range(2):
        move(i,tg)

for i in range(n):
    for j in range(n):

        # 세로바꾸기
        if 0 <= i + 1 < n and 0 <= j < n:
            change(i,j,i+1,j)

        # 가로 바꾸기
        if 0 <= i < n and 0 <= j + 1 < n:
            change(i,j,i,j+1)

print(ans)