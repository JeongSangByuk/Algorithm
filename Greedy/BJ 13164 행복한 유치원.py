import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline

n, k = map(int,input().split())
g = list(map(int, input().split()))

space = []

for i in range(1, len(g)):
    space.append(g[i] - g[i-1])

# print(g)
# print(space)

space.sort(reverse=True)

print(sum(space[k-1:]))



















