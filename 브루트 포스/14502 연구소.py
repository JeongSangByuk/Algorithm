
import collections

# https://wookcode.tistory.com/141

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
nowMax = 0

def bfs():
    global nowMax
    check = [[-1] * m for _ in range(n)]

    # 상하좌우 이동을 위한 변수
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = collections.deque()

    # 바이러스를 모두 돌아주기 위해 큐에 바이러스 넣기
    for x in range(n):
        for y in range(m):
            if g[x][y] == 2:
                queue.append((x,y))
                check[x][y] = 0

    while queue:
        x,y = queue.popleft()

        # 4가지 방향향
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            # 그래프 범위 내에 있는지,
            # 0이고 방문 안한곳인지 확인
            if 0 <= nx < n and 0 <= ny < m:
                if g[nx][ny] == 0 and check[nx][ny] == -1:

                    # 즉 바이러스를 퍼트린다.
                    queue.append((nx,ny))
                    check[nx][ny] = 0

    # 바이러스가 다 퍼진 후, 안전 영역 count
    count = 0
    for x in range(n):
        for y in range(m):
            if g[x][y] == 0 and check[x][y] == -1:
                count += 1

    nowMax = max(nowMax, count)


#3개의 벽을 세우는 모든 경우의 수
def recursive(i):

    # 3개면 탈출
    if i == 3:
        bfs()
        return

    for x in range(n):
        for y in range(m):

            # 일반 구역이라면, 벽을 세워서 다음으로 넘어간다.
            if g[x][y] == 0:
                g[x][y] = 1
                recursive(i + 1)

                # 재귀가 끝난 후 벽 초기화
                g[x][y] = 0


recursive(0)

print(nowMax)