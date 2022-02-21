import sys
import heapq
from collections import deque, defaultdict
import itertools

input = sys.stdin.readline

# 상하좌우
dy, dx = [1,-1,0,0], [0,0,-1,1]

h, w = map(int, input().split())

g = [list(input().strip()) for _ in range(h)]
answer = 0

#print(g)

history = set()

def dfs(y, x, cnt) :
    global answer
    answer = max(answer, cnt)

    for i in range(4):

        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= nx < w and 0 <= ny < h and not g[ny][nx] in history:
            history.add(g[ny][nx])
            dfs(ny,nx, cnt + 1)
            history.remove(g[ny][nx])

# dfs 풀이
history.add(g[0][0])
dfs(0,0,1)

print(answer)