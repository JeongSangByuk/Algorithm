import math
import sys
from collections import deque
from collections import defaultdict
import itertools
from heapq import heappop, heappush
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
g = list(tuple(map(int, input().split())) for _ in range(n))

g.sort(key=lambda x: (x[0], x[1]))

heap = list()

result = 0

for i in g:

    if not heap or heap[0] > i[0]:
        heappush(heap, i[1])
        result += 1
        continue

    heappop(heap)
    heappush(heap, i[1])

print(result)