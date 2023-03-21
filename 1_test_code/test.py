import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

input = sys.stdin.readline

m, n, h = map(int, input().split())
g =  list(list(list(map(int, input().split())) for _ in range(n)) for _ in range(h))

dy, dx = [1, -1, 0, 0], [0, 0, -1, 1]
que = deque()
answer = 0

print(g)
