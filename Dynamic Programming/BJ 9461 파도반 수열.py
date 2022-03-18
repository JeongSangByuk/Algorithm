import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

#1,1,1,2,2,3,4,5,7,9,12,16

n = int(input())
ans = []

for i in range(n):
    dp = [0] * 101

    dp[0] = 1
    dp[1] = 1
    dp[2] = 1

    k = int(input())
    for i in range(3,k):
        dp[i] = dp[i-3] + dp[i-2]

    ans.append(dp[k - 1])

print(*ans, sep='\n')
