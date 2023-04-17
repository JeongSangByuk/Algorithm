import math
import sys
from collections import deque
from collections import defaultdict
import itertools
from heapq import heappop, heappush
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n = int(input())
g = list(list(map(str, input().strip())) for _ in range(n))

dic = defaultdict(int)

for i in range(n):

    l = len(g[i])
    tl = l - 1
    for j in range(l):
        dic[g[i][j]] += (10 ** tl)
        tl -= 1

heap = list()

for i in dic:
    heappush(heap, (-dic[i], dic[i], i))

c = 9
result = 0
while heap:
    t = heappop(heap)
    result += (t[1] * c)
    c -= 1

    if c == 0:
        break
print(result)