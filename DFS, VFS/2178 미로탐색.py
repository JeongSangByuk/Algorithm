from collections import deque

n, m  = map(int, input().split())
g = [list(map(int, input())) for _ in range(n)]

# 상하좌우 이동을 위한 변수
d = [[-1, 0], [1, 0], [0, 1], [0, -1]]

visited = [[0] * m for _ in range(n)]

answer = []

def bfs(x,y):

    que = deque()
    que.append([y,x,0])
    visited[y][x] = 1

    while que:

        node = que.popleft()

        # 큐에 상하좌우 이동한 값 넣어주기
        for i in range(4):
            ny = node[0] + d[i][0]
            nx = node[1] + d[i][1]
            cnt = node[2]
            if 0 <= ny < n and 0 <= nx < m:
                print(ny, nx)
                if g[ny][nx] == 1 and visited[ny][nx] == 0:

                    # 답
                    if nx == m-1 and ny == n-1:
                        return cnt + 2

                    que.append([ny,nx,cnt+1])
                    visited[ny][nx] = 1

print(bfs(0,0))




