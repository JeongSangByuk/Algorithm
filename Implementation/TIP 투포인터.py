import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline

# 수열에서 합이 m이 되는 경우,

n, m = map(int, input().split())
g = list(map(int, input().split()))

s = 0
end = 0
cnt = 0

for start in range(n):

    while end < n and s < m:
        s += g[end]
        end += 1

    if s == m:
        cnt += 1

    s -= g[start]

print(cnt)
