import sys
import heapq
from collections import deque, defaultdict
import itertools

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

dy, dx = [-1,1,0,0],[0,0,-1,1]

n, m, k = map(int, input().split())

g = [[0]*m for _ in range(n)]

for i in range(k):
    p = list(map(int, input().split()))

    w = p[2] - p[0]
    h = p[3] - p[1]

    p[3] = n - p[3]
    for y in range(p[3], p[3] + h):
        for x in range(p[0], p[0] + w):
            g[y][x] = 1

visited = set()

def dfs(y,x,answer):

    for i in range(4):

        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m and not (ny,nx) in visited and\
            g[ny][nx] != 1:

            g[ny][nx] = 1
            visited.add((ny,nx))
            print(answer)
            answer = dfs(ny,nx, answer + 1)

    return answer

cnt = 0
box_num = []

for i in range(n):
    for j in range(m):

        if not (i,j) in visited and g[i][j] == 0:
            visited.add((i,j))
            a = dfs(i,j,0)
            cnt += 1
            box_num.append(a + 1)

print(cnt)

box_num.sort()
box_num = list(map(str, box_num))
print(' '.join(box_num))