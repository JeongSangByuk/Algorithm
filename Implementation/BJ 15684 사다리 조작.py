import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq

n, m, h = map(int, input().split())
visited = [[False] * (n+1) for _ in range(h+1)]

ladder = []

for _ in range(m):
    a, b = map(int, input().split())
    visited[a][b] = True

def check():
    for i in range(1, n + 1):
        now = i

        for j in range(1, h + 1):
            if visited[j][now-1]:
                now -= 1
            elif visited[j][now]:
                now += 1

        if now != i:
            return False

    return True


def dfs(depth, idx):
    global ans

    if depth >= ans:
        return

    if check():
        ans = depth
        return
    for l in range(idx, l_len):
        y, x = ladder[l]

        if not visited[y][x-1] and not visited[y][x+1]:
            visited[y][x] = True
            dfs(depth + 1, l + 1)
            visited[y][x] = False

for i in range(1, h + 1):
    for j in range(1, n):
        if not visited[i][j-1] and not visited[i][j] and not visited[i][j+1]:
            ladder.append((i, j))
ans = 4

l_len = len(ladder)

dfs(0,0)

print(ans if ans < 4 else -1)