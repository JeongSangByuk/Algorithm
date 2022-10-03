import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline


n = int(input())

def bfs():
    que = deque()
    que.append((1,0,0))
    visited = set()
    visited.add((1,0,0))

    while que:
        #print(que)
        display, clib_board, cnt = que.popleft()

        if display == n:
            return cnt

        # 화면 to 클립보드
        if display > 0 and (display, display, cnt+1) not in visited:
            que.append((display, display, cnt+1))
            visited.add((display, clib_board, cnt + 1))

        # 클립보드 to 화면
        if clib_board > 0 and (display + clib_board, clib_board, cnt+1) not in visited:
            que.append((display + clib_board, clib_board, cnt+1))
            visited.add((display + clib_board, clib_board, cnt + 1))

        if display > 0 and (display - 1, clib_board, cnt+1) not in visited:
            que.append((display - 1, clib_board, cnt+1))
            visited.add((display - 1, clib_board, cnt+1))



print(bfs())
