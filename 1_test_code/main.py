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

for i in g:
    for j in i:
        if j == 1:
            cheese_cnt += 1
            cheese.append((i,j))
        else:
            normal.add((i,j))


def bfs():
    cnt = 0

    while cheese:
        cy,cx = cheese.popleft()
        tmp = 0

        for i in range(4):
            if (cy,cx) in normal:
                tmp += 1

        if tmp >= 2:
            normal.add(cy,cx)


        # 안없어진 경우
        else:
            cheese.append((cy,cx))




bfs()











