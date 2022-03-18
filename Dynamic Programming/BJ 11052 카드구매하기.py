import sys
from collections import deque
import itertools
import heapq

# https://jyeonnyang2.tistory.com/56
# DP의 접근은 문제의 작은 부분부터!

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
g = list(map(int, input().split()))

dp = [0]*(n + 1)
for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i],g[j - 1] + dp[i - j])

print(dp[n])