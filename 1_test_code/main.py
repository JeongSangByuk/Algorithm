import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())
g = list(list(map(int, input().split())) for _ in range(n))

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]


