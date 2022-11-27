import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
dp = [5001] * (5001)
dp[3] = 1
dp[5] = 1
_max = 100000

for i in range(6, n + 1):
    a = dp[i - 3]
    b = dp[i - 5]
    dp[i] = min(a, b) + 1

result = -1 if dp[n] >= 5001 else dp[n]
print(result)

