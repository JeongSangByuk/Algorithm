import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline

n = int(input())
k = int(input())
g = list(set(map(int, input().split())))
g.sort()

space = []

for i in range(1, len(g)):
    space.append(g[i] - g[i-1])

# print(g)
# print(space)

for i in range(k - 1):

    if len(space) > 0:
        space.remove(max(space))
    #print(space)

print(sum(space))



















