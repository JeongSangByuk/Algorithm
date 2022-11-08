import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

m, n = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

# 서북동남
dy, dx = [0, -1, 0, 1], [-1, 0, 1, 0]
k = [0, 1, 2, 3]
num = [1,2,4,8]

visited = set()
wall = set()

def check(y, x, i):

    if g[y][x] & (1 << k[i]):
        return False
    else:
        return True

def dfs(y, x, cnt):

    a = cnt

    for i in range(4):

        ny = y + dy[i]
        nx = x + dx[i]

        # 갈수 있는 경우만,
        if 0 <= ny < n and 0 <= nx < m and check(y, x, i) and (ny, nx) not in visited:
            visited.add((ny, nx))
            a = dfs(ny, nx, a + 1)

    return a


def search():
    ans = 0
    ans2 = 0

    for i in range(n):
        for j in range(m):

            if (i, j) not in visited:
                visited.add((i, j))
                ans2 = max(dfs(i, j, 1), ans2)
                ans += 1

    return ans,ans2


result = search()
print(result[0])
print(result[1])

# print(wall)

ans3 = result[1]

for i in range(n):
    for j in range(m):

        for c in range(4):

            if not check(i,j,c):

                g[i][j] -= num[k[c]]

                visited.clear()

                visited.add((i, j))
                ans3 = max(ans3, dfs(i,j,1))

                g[i][j] += num[k[c]]

print(ans3)