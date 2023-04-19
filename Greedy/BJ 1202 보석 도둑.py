import math
import sys
from collections import deque
from collections import defaultdict
import itertools
from heapq import heappop, heappush
from bisect import bisect_left

input = sys.stdin.readline

n, k = map(int, input().split())
dia = list(tuple(map(int, input().split())) for _ in range(n))
bag = list(int(input()) for _ in range(k))

dia.sort()
bag.sort()

result = 0
now = 0
tmp_b = list()

# 담을 수 있는거 다 담아놓고, 가장 높은거 꺼내쓰자는 개념

for i in range(k):

    while now < n:

        if dia[now][0] <= bag[i]:
            heappush(tmp_b, (-dia[now][1], dia[now][0]))
            now += 1
            continue
        break

    if tmp_b:
        result += -heappop(tmp_b)[0]

print(result)