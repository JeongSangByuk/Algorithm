import sys
from collections import deque
import itertools
import heapq

n, m = map(int, input().split())
g = list(map(int, input().split()))

c = list(itertools.combinations(g,3))
l = 10

for i in c:
    if l <= sum(i) <= m:
        l = sum(i)

print(l)





