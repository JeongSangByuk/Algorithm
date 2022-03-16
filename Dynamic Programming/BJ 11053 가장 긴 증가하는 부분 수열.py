import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
g = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):

        if g[j] < g[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))