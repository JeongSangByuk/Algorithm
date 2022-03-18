import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
dp = [0] * n
dp[0] = 1

if n > 1:
    dp[1] = 2

    for i in range(2,n):
        dp[i] = (dp[i-2] + dp[i - 1]) % 15746

print((dp[n-1]) % 15746)