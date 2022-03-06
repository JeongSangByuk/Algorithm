import sys
from collections import deque
import itertools

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())

g = [list(map(int, input().strip())) for _ in range(n)]

# visited 배열을 벽을 뿌신 경로와 아닌 경로 두개로 설정.
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dy, dx = [-1,1,0,0],[0,0,-1,1]

def bfs():

    # 벽을 부시기 사용한 경우 0, or 1
    que = deque()
    que.append((0,0,1))
    visited[0][0][1] = 1

    while que:
        y,x,crash = que.popleft()

        if y == n - 1 and x == m - 1:
            return visited[y][x][crash]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < m and 0 <= ny < n:

                # 벽 부시고 이동
                if g[ny][nx] == 1 and crash == 1:
                    visited[ny][nx][0] = visited[y][x][1] + 1
                    que.append((ny, nx, 0))

                # 이미 방문한 경우 최단 경로가 될 수 없기 때문에,
                elif g[ny][nx] == 0 and visited[ny][nx][crash] == 0:
                    visited[ny][nx][crash] = visited[y][x][crash] + 1
                    que.append((ny, nx, crash))

    return -1

print(bfs())




