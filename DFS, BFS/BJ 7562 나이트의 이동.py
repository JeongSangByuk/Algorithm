import sys
import heapq
from collections import deque, defaultdict
import itertools

sys.setrecursionlimit(10**7)

input = sys.stdin.readline

n = int(input())

dy, dx = [-1,-2,-2,-1,1,2,2,1],[-2,-1,1,2,-2,-1,1,2]

answer = []

for case in range(n):

    k = int(input())

    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    que = deque()
    que.append((start_x,start_y,0))

    visited = set()
    visited.add((start_x,start_y))

    while que:
        x, y, cnt = que.popleft()

        if x == end_x and y == end_y:
            answer.append(cnt)
            break

        for i in range(8):

            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < k and 0 <= ny < k and (nx,ny) not in visited:
                que.append((nx,ny,cnt + 1))
                visited.add((nx,ny))


print(*answer, sep = '\n')


