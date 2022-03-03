import sys
import heapq
from collections import deque, defaultdict
import itertools

sys.setrecursionlimit(10**7)

input = sys.stdin.readline

n, m = map(int, input().split())

g = [list(input().strip()) for _ in range(n)]

dy, dx = [-1,1,0,0],[0,0,-1,1]

def bfs():

    que = deque()
    visited = set()
    visited.add((0,0))
    que.append((0,0,visited,1))

    while que :

        print(que)

        y, x,tmp_visited,cnt = que.popleft()

        for i in range(4):

            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and (ny, nx) not in tmp_visited and g[ny][nx] == '0':

                if ny == n - 1 and nx == m - 1:
                    return cnt + 1

                v = tmp_visited.copy()
                v.add((ny,nx))
                que.append((ny,nx,v,cnt + 1))

print(bfs())