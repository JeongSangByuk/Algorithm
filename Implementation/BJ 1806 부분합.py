import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
g = list(map(int, input().split()))

s = 0
end = 0
answer = 1e9

for start in range(n):

    while end < n and s < m:
        s += g[end]
        end += 1

    if s >= m and (end - start) < answer:
        answer = (end - start)

    s -= g[start]

if answer == 1e9:
    print(0)
else:
    print(answer)


