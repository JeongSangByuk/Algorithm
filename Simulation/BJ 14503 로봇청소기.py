import copy
import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())

y, x, d = map(int, input().split())

g = [list(map(int, input().split())) for _ in range(n)]
visited = g[:]

# 0,1,2,3
# 좌하우상, 상좌하우, 우상좌하, 하우상좌


# dy = [[0,1,0,-1,1],[-1,0,1,0,0],[0,-1,0,1,-1],[1,0,-1,0,0]]
# dx = [[-1,0,1,0,0],[0,-1,0,1,-1],[1,0,-1,0,0],[0,1,0,-1,1]]

dy,dx = [-1,0,1,0],[0,1,0,-1]

def solution():
    global y,x,d

    answer = 0

    while True:

        # 1

        if g[y][x] == 0:
            answer += 1
            g[y][x] = 2

        #print(visited,y,x,d)
        # 2-1

        isFinished = False

        cnt = 0

        for i in range(4):

            ny = y + dy[(d + 3 -i)%4]
            nx = x + dx[(d + 3 -i)%4]
            cnt += 1

            if g[ny][nx] == 0:
                y = ny
                x = nx
                isFinished = True

                k = d - cnt

                if k < 0:
                    k += 4

                d = k

                break

        # 이동 완료
        if isFinished:
            continue

        # 2-3
        ny = y + dy[(d + 2) % 4]
        nx = x + dx[(d + 2) % 4]

        if g[ny][nx] == 1:
            return answer
        else:
            y = ny
            x = nx
            continue

        return answer


print(solution())











