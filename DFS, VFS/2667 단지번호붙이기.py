from collections import deque


n = int(input())
g = [list(map(int, input())) for _ in range(n)]

# 상하좌우 이동을 위한 변수
d = [[-1, 0], [1, 0], [0, 1], [0, -1]]

visited = [[0] * n for _ in range(n)]

total = 0

answer = []

def bfs(x,y):

    que = deque()
    que.append([x,y])
    visited[x][y] = 1
    cnt = 1

    while que:

        node = que.popleft()

        # 큐에 상하좌우 이동한 값 넣어주기
        for i in range(4):
            nx = node[0] + d[i][0]
            ny = node[1] + d[i][1]

            if 0 <= nx <n and 0<= ny < n:
                if g[nx][ny] == 1 and visited[nx][ny] == 0:
                    que.append([nx,ny])
                    visited[nx][ny] = 1
                    cnt += 1

    answer.append(cnt)

for x in range(n):
    for y in range(n):
        if g[x][y] == 1 and visited[x][y] == 0:
            bfs(x,y)
            total += 1

print(total)
answer.sort()
for i in answer:
    print(i)


