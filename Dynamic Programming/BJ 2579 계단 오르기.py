import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())

arr = [int(input()) for _ in range(n)] + [0]

# n이 1인 경우 때문에,
dp = [0] * (n + 2)

dp[1] = arr[0]
dp[2] = arr[1] + arr[0]

for i in range(3, n + 1):
    dp[i] = max(dp[i - 2], arr[i - 2] + dp[i - 3]) + arr[i - 1]

print(arr)
print(dp)
print(dp[n])