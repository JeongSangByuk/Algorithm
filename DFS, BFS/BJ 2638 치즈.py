import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline


n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
dy, dx = [-1,1,0,0], [0,0,-1,1]

cheese = deque()
normal = set()
cheese_cnt = 0

for i in range(n):
    for j in range(m):

        if g[i][j] == 1:
            cheese_cnt += 1
            cheese.append((i,j))

def check_inner_cheese():

    visited = set()

    que = deque()
    que.append((0,0))
    visited.add((0,0))

    while que:

        ny,nx = que.popleft()

        for i in range(4):
            y = ny + dy[i]
            x = nx + dx[i]

            if 0 <= y < n and 0 <= x < m and (y,x) not in visited and g[y][x] == 0:

                que.append((y,x))
                visited.add((y,x))

    return visited

def bfs():

    global cheese_cnt
    cnt = 0

    while cheese_cnt > 0:

        cnt += 1
        tmp_cnt = cheese_cnt
        normal = check_inner_cheese()
        j = 0

        while j <= tmp_cnt and cheese:

            #print(cheese, cnt)

            cy,cx = cheese.popleft()
            j += 1

            tmp = 0

            # 사분면 검사
            for i in range(4):
                if (cy + dy[i], cx + dx[i]) in normal:
                    tmp += 1

            # 없어질 경우
            if tmp >= 2:
                cheese_cnt -= 1
                g[cy][cx] = 0

            # 안없어진 경우, 다시 넣어주기.
            else:
                cheese.append((cy,cx))

    return cnt

print(bfs())












