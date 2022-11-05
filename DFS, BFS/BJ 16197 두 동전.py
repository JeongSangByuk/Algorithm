import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())

g = [list(map(str, input().strip())) for _ in range(n)]

dy,dx = [-1,1,0,0], [0,0,-1,1]
a,b = (0,0), (0,0)
DROP = -10000

tmp = True

for i in range(n):
    for j in range(m):

        if g[i][j] == 'o' and tmp:
            a = (i,j)
            tmp = False

        elif g[i][j] == 'o' and not tmp:
            b = (i, j)
            break


def move(t, y, x):

    ny = y + dy[t]
    nx = x + dx[t]

    if 0 <= ny < n and 0 <= nx < m:

        # 벽일 경우 유지
        if g[ny][nx] == '#':
            return (y,x)

        return (ny,nx)

    return (DROP,DROP)

def bfs():

    que = deque()
    que.append((a,b,0))

    while que:

        na,nb,cnt = que.popleft()

        if cnt > 9:
            return -1

        for i in range(4):
            ta = move(i, na[0], na[1])
            tb = move(i, nb[0], nb[1])

            # 둘다 떨구는 경우 pass
            if ta[0] == DROP and tb[0] == DROP:
                continue

            # 둘중 하나만 떨구는 경우
            if (ta[0] == DROP and tb[0] != DROP) or (ta[0] != DROP and tb[0] == DROP):
                return cnt + 1

            # 둘다 일치하는 경우 pass
            if ta == na and tb == nb:
                continue

            que.append((ta,tb,cnt + 1))

    return -1

print(bfs())











