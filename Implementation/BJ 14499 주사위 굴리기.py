import copy
import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n,m,x,y,k = map(int,input().split())

g = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]

def move(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1: #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c

    elif dir == 2: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d

    elif dir == 3: #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b

    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

nx, ny = x, y

for i in order:
    nx += dx[i - 1]
    ny += dy[i - 1]

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        nx -= dx[i - 1]
        ny -= dy[i - 1]
        continue
    move(i)
    if g[nx][ny] == 0:
        g[nx][ny] = dice[-1]
    else:
        dice[-1] = g[nx][ny]
        g[nx][ny] = 0

    print(dice[0])






















