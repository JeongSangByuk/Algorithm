import math
import sys
from collections import deque
from collections import defaultdict
import itertools
from heapq import heappush, heappop
from bisect import bisect_left

input = sys.stdin.readline

n, k = map(int, input().split())
g = list(map(int, input().split()))
tap = set()

lg = len(g)
cnt = 0
for i in range(lg):

    # print(tap)

    if g[i] in tap:
        continue

    # 남은 경우
    if len(tap) < n:
        tap.add(g[i])
        continue

    tmp_l = list()
    v = tap.copy()

    for j in range(i + 1, lg):

        if len(v) == 1:
            break

        if g[j] in v:
            v.remove(g[j])

    # print(v, "qweqew")
    tap.remove(v.pop())
    tap.add(g[i])
    cnt += 1

# print(tap)
print(cnt)
