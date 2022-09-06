import copy
import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())

k = int(input())

g = [[0] * n for _ in range(n)]
d = deque()

for i in range(k):
    y, x = map(int, input().split())

    # 사과
    g[y-1][x-1] = 1

l = int(input())

for i in range(l):
    x, c = map(str, input().split())
    d.append((int(x),c))

# 뱀위치
sx,sy = 0,0

# 상하좌우
dy,dx = [-1,1,0,0],[0,0,-1,1]

nowWay = 3

def moveL():
    global nowWay

    if nowWay == 0:
        nowWay = 2
    elif nowWay == 1:
        nowWay = 3
    elif nowWay == 2:
        nowWay = 1
    elif nowWay == 3:
        nowWay = 0

def moveD():
    global nowWay

    if nowWay == 0:
        nowWay = 3
    elif nowWay == 1:
        nowWay = 2
    elif nowWay == 2:
        nowWay = 0
    elif nowWay == 3:
        nowWay = 1

time = 0

snake_len = 1

snake_stack = deque()
snake_stack.append([sy,sx])

while True:

    if d and d[0][0] == time:
        if d[0][1] == 'D':
            moveD()
        elif d[0][1] == 'L':
            moveL()
        d.popleft()

    time += 1

    ori_y = snake_stack[-1][0]
    ori_x = snake_stack[-1][1]

    sy = ori_y + dy[nowWay]
    sx = ori_x + dx[nowWay]

    if sy < 0 or sy >= n or sx < 0 or sx >= n:
        print(time)
        break

    # 사과 먹은 경우
    if g[sy][sx] == 1:

        snake_stack.append([sy,sx])
        g[sy][sx] = 0
        snake_len += 1

        if [sy, sx] in list(itertools.islice(snake_stack, 0, snake_len - 1)):
            print(time)
            break

    # 그냥 이동
    else :
        # 새로운 위치 다 업데이트

        snake_stack.append([sy,sx])

        if [sy, sx] in list(itertools.islice(snake_stack, 0, snake_len - 1)):
            print(time)
            break

        snake_stack.popleft()





















