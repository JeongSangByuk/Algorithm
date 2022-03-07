import sys
from collections import deque
import itertools

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m  = map(int, input().split())

g = [list(map(str, input().strip())) for _ in range(n)]

# 상하좌우
dy, dx = [-1,1,0,0],[0,0,-1,1]

# 중복 방지
visited = set()

red_init = [0,0]
blue_init = [0,0]

# 첫 시작 찾기.
for i in range(n):
    for j in range(m):
        if g[i][j] == 'R':
            red_init[0] = i
            red_init[1] = j
        elif g[i][j] == 'B':
            blue_init[0] = i
            blue_init[1] = j

def move_ball(y,x,i):

    cnt = 0

    while g[y + dy[i]][x + dx[i]] != '#' and g[y][x] != 'O':
        y += dy[i]
        x += dx[i]
        cnt += 1

    return (y,x,cnt)


def bfs():

    que = deque()
    que.append((red_init[0],red_init[1],blue_init[0],blue_init[1],0))

    while que:
        ry, rx, by, bx, cnt = que.popleft()
        visited.add((ry, rx, by, bx))

        if cnt >= 10:
            return -1

        for i in range(4):
            nry, nrx, rcnt = move_ball(ry, rx, i)
            nby, nbx, bcnt = move_ball(by, bx, i)

            if g[nby][nbx] != 'O':

                # 탈출
                if g[nry][nrx] == 'O':
                    return cnt + 1

                # 겹쳤을 때, 먼저 온애를 찾는다
                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]

                if (nry,nrx,nby,nbx) not in visited:
                    visited.add((nry,nrx,nby,nbx))
                    que.append((nry,nrx,nby,nbx,cnt + 1))
    return -1

print(bfs())













