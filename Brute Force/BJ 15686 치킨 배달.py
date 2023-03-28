import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())
g = list(list(map(int, input().split())) for _ in range(n))

chick = []
home = []

for i in range(n):
    for j in range(n):
        if g[i][j] == 2:
            chick.append((i, j))
        elif g[i][j] == 1:
            home.append((i, j))

visit = set()


def calculate(visit):

    result = 0
    for h in home:

        result += min(list(abs(h[0] - v[0]) + abs(h[1] - v[1]) for v in visit))

    return result


result = 9e9

tmp = list([-1] * n for _ in range(n))


cl = len(chick)

# 조합을 백트래킹으로 구현하는 방법
def dfs(ori_idx, cnt):

    global result

    if cnt == m:
        result = min(result, calculate(visit))
        return

    for i in range(ori_idx + 1, cl):

        visit.add(chick[i])
        dfs(i, cnt + 1)
        visit.remove(chick[i])

for i in range(cl):

    visit.add(chick[i])
    dfs(i, 1)
    visit.remove(chick[i])


# 조합을 통한 풀이
# c = list(itertools.combinations(chick, m))
# result = 9e9
# for i in c:
#     result = min(result, calculate(i))

print(result)
