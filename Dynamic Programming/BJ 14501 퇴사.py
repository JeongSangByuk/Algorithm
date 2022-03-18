import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
g = []


for i in range(n):
    time, pay = map(int, (input().split()))
    g.append((time,pay))


# 내 풀이
# dp = [0] * n
# dp[0] = g[0][1]
#
# for i in range(n):
#
#     m = 0
#     for j in range(0,i + 1):
#         if j + g[j][0] - 1 < i and m < dp[j]:
#             m = dp[j]
#
#     dp[i] = m
#     if i + g[i][0] - 1 < n:
#         dp[i] += g[i][1]
#     # print(i, dp)
#print(max(dp))

# 정석 풀이
dp = [0] * (n + 1)

for i in range(n - 1, -1 , -1):

    if i + g[i][0] > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(g[i][1] + dp[i + g[i][0]], dp[i+1])

print(dp)






