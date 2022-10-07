import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline

n = int(input())
g = list(map(int,input().split()))

g.sort()

start = 0
end = n - 1
m = 2e9
a1, a2 = 0, 0

while start < end:

    s = g[start] + g[end]

    if abs(s) < m:
        m = abs(s)
        a1, a2 = g[start], g[end]

    if s > 0:
        end -= 1
    else:
        start += 1

print(a1,a2)













