import sys
import heapq
from collections import deque, defaultdict
import itertools

input = sys.stdin.readline

# 상하좌우
dy, dx = [1,-1,0,0], [0,0,-1,1]

h, w = map(int, input().split())

g = [input().strip() for _ in range(h)]
answer = 0

def bfs():

    global answer

    que = deque()

    history = [0] * 26
    history[ord(g[0][0]) - ord('A')] = 1

    que.append([(0,0),history,0])

    while que:

        print(que)

        # node[0] = y,x , node[1] = history, node[2] = cnt
        node = que.popleft()

        for i in range(4):

            y = node[0][0] + dy[i]
            x = node[0][1] + dx[i]

            if y < 0 or y >= h:
                continue

            if x < 0 or x >= w:
                continue

            if node[1][ord(g[y][x]) - ord('A')] == 0:

                tmp_history = node[1][:]
                answer = node[2] + 1

                tmp_history[ord(g[y][x]) - ord('A')] = 1
                que.append([(y,x), tmp_history, node[2] + 1])

bfs()

print(answer)