import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())

dp = [0] * 1000

dp[0] = 1
dp[1] = 3

for i in range(2, n):
    dp[i] = dp[i-2] * 2 + dp[i-1]

print(dp[n-1])