import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

input = sys.stdin.readline

N = 5

# 오리지널
board = [[i * N + j for j in range(N)] for i in range(N)]
print(*board, sep="\n")
print("\n")

# 시계
rotated_2 = list(map(list, zip(*board[::-1])))
print(*rotated_2,sep="\n")
print("\n")

# 반시계
rotated_1 = list(map(list, zip(*board)))[::-1]
print(*rotated_1,sep="\n")
print("\n")

