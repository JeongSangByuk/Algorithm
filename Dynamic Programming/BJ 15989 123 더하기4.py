import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 6)

n = int(input())

dp = [1]*(10001)

for i in range(2, 10001):
    dp[i] += dp[i - 2]

for i in range(3, 10001):
    dp[i] += dp[i - 3]

for _ in range(n):
    t = int(input())
    print(dp[t])















