import math
import sys
from collections import deque, defaultdict
import itertools
from heapq import heappush, heappop

input = sys.stdin.readline

n, m = map(int, input().split())
g = list(list(map(int, input().split())) for _ in range(n))
c = list(list(map(int, input().split())) for _ in range(m))

# dp 배열은 (0,0) ~ (y,x)을 표현.
dp = list([0] * (n + 1) for _ in range(n + 1))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = g[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

for i in c:
    ay, ax, by, bx = i[0], i[1], i[2], i[3]
    ans = dp[by][bx] - dp[by][ax - 1] - dp[ay - 1][bx] + dp[ay - 1][ax - 1]
    print(ans)
