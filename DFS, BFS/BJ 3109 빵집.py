import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

r, c = map(int, input().split())
g = [list(map(str, input().strip())) for _ in range(r)]
dy, dx = [-1,0,1],[-1,-1,-1]
answer = 0

def dfs(y,x):

    global answer

    g[y][x] = 'x'

    if x == 0:
        answer += 1
        return True

    for i in range(3):

        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < r and 0 <= nx < c and g[ny][nx] == '.':

            if dfs(ny,nx):
               return True

    return False

for i in range(r):


    dfs(i,c-1)

print(answer)


