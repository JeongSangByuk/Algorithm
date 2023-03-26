import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

r, c = map(int, input().split())
g = list(list(input().strip()) for _ in range(r))

# visit = set()
is_finish = False
ans = 0

def dfs(y, x):
    global is_finish, ans
    # print(y,x)

    if x == c - 1:
        is_finish = True
        ans += 1

    if is_finish:
        return

    x = x + 1
    for i in [y - 1, y, y + 1]:

        if not (0 <= i < r and 0 <= x < c and g[i][x] == '.'):
            continue

        g[i][x] = 'X'
        dfs(i, x)

        if is_finish:
            return

        # visit.remove((i, x))


for i in range(r):
    is_finish = False
    g[i][0] = 'X'
    dfs(i, 0)
    # print("-------")


print(ans)
