import sys
import heapq
from collections import deque, defaultdict
import itertools

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m = map(int, input().split())

g = [list(map(int, input().split())) for _ in range(n)]

dy, dx = [0,0,1,-1],[1, -1, 0,0]

visited = [[-1 for _ in range(m)] for _ in range(n)]

def dfs(y,x):

    if y == (n - 1) and x == (m - 1):
        return 1

    # -1이 아닌 경우 한번은 접근한 경로로 볼 수 있다.
    if visited[y][x] != -1:
        return visited[y][x]

    visited[y][x] = 0

    for i in range(4):

        ny = y + dy[i]
        nx = x + dx[i]

        # 접근 가능할때만 해당 경로에서 Dfs 돌린다.
        if 0 <= ny < n and 0 <= nx < m and g[y][x] > g[ny][nx]:

            visited[y][x] += dfs(ny,nx)

    return visited[y][x]

print(dfs(0,0))

print(visited)



