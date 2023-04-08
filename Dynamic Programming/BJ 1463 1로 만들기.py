import sys
from collections import deque

input = sys.stdin.readline().strip

n = int(input())

_max = n + 4
dp = [_max] * _max

dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, n + 1):

    a, b, c = _max, _max, _max

    if i % 2 == 0:
        a = dp[i//2]
    if i % 3 == 0:
        b = dp[i//3]
    c = dp[i - 1]

    dp[i] = min(a,b,c) + 1

print(dp[n])


