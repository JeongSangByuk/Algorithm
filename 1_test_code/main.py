import sys
from collections import deque
import itertools

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())

g = [list(map(int, input().split())) for _ in range(n)]

# 위부터 갔다가, 왼쪽으로 가는 루트로,,
dy, dx = [-1,0,0,1],[0,-1,1,0]
sx, sy = 0, 0

# 아기 상어 첫 시작 위치
for i in range(n):
    for j in range(n):
        if g[i][j] == 9:
            sy, sx = i, j

now_shark = 2
tmp_shark = 0
answer = 0

# 먹을 고기가 있는지 없는지 탐색
def is_fin(now_shark):

    for i in range(n):
        for j in range(n):
            if g[i][j] < now_shark and g[i][j] != 0:
                return False

    return True

def bfs():

    global now_shark,tmp_shark
    global answer

    que = deque()
    que.append((sy,sx,0))
    g[sy][sx] = 0

    visited = set()
    visited.add((sy, sx))

    # 먹이 값 넣어놓고
    tmp_fish = []

    while que:

        if is_fin(now_shark):
            return

        # print(que)
        # print(visited)
        # print(tmp_fish)
        y, x, cnt = que.popleft()

        # 저장된 먹이 리스트에서 우선순위 높은 먹이 찾기 위해
        if (tmp_fish and tmp_fish[0][2] < cnt):

            # 우선순위에 따른 정렬
            tmp_fish.sort(key = lambda x: (x[0],x[1]))

            ny, nx, cnt = tmp_fish[0][0], tmp_fish[0][1], tmp_fish[0][2]

            g[ny][nx] = 0

            tmp_shark += 1

            # 상어 레벨업!
            if tmp_shark == now_shark:
                now_shark += 1
                tmp_shark = 0

            # 다시 BFS 돌리기 위해
            que.clear()
            visited.clear()
            tmp_fish.clear()

            que.append((ny, nx, 0))
            visited.add((ny, nx))

            answer += (cnt + 1)
            # print(ny, nx, answer)
            continue

        for i in range(4):

            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n and now_shark >= g[ny][nx]\
                    and (ny, nx) not in visited:

                # 먹을수 있는 물고기 발견, 일단은 리스트에 넣기
                if g[ny][nx] < now_shark and g[ny][nx] != 0:
                    tmp_fish.append((ny,nx,cnt))

                visited.add((ny,nx))
                que.append((ny,nx,cnt + 1))


bfs()
print(answer)





