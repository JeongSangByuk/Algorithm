import sys
from collections import deque
import itertools

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())

g = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1]*n for _ in range(n)]

# 상하좌우
dy, dx = [-1,1,0,0],[0,0,-1,1]

def dfs(y,x):

    answer = 1

    for i in range(4):

        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < n and g[y][x] < g[ny][nx] :

            # 다음 노드가 방문하지 않은 노드면 방문
            if visited[ny][nx] == -1:
                visited[ny][nx] = dfs(ny, nx)

            if answer < visited[ny][nx] + 1:
                answer = visited[ny][nx] + 1

    return answer

a = 0

for i in range(n):
    for j in range(n):

        # 탐색하지 않은 부분만 dfs
        if visited[i][j] == -1 :
            visited[i][j] = 0
            visited[i][j] = dfs(i,j)

            # 최장 거리 갱신
            if a < visited[i][j]:
                a = visited[i][j]
print(visited)
print(a)