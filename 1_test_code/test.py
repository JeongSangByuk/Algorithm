import copy
import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m  = map(int, input().split())

g = [list(map(int, input().split())) for _ in range(n)]

# dfs 활용
# https://cijbest.tistory.com/87

maxValue = 0

dy, dx = [-1,1,0,0], [0,0,-1,1]

visited = [[-1] * m for _ in range(n)]

maxValueInG = max(map(max, g))

# ㅗ, ㅜ, ㅓ, ㅏ 제외한 모양들 최대값 계산
def dfs(y,x,dSum, cnt):

    global maxValue

    # 가지 치기
    if maxValue >= dSum + maxValueInG * (4-cnt):
        return

    if cnt == 4:
        maxValue = max(maxValue,dSum)
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == -1:

            if cnt == 2:
                visited[ny][nx] = 0
                dfs(y, x, dSum + g[ny][nx], cnt + 1)
                visited[ny][nx] = -1

            visited[ny][nx] = 0
            dfs(ny,nx,dSum + g[ny][nx], cnt + 1)
            visited[ny][nx] = -1

for i in range(n):
    for j in range(m):
        visited[i][j] = 0
        dfs(i,j,g[i][j],1)
        visited[i][j] = -1

print(maxValue)


