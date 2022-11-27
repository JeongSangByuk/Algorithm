import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
g = [int(input()) for _ in range(n)] + [0] * 10000

# dp 배열 -> 해당 계단을 밟았을 때의 최댓값
# 포도주 문제와의 차이점. -> 반드시, 1칸 or 2칸만을 이동해야함. 즉 해당 dp index에서 밟음을 전제.
# but, 포도주 문제 -> 여러칸을 한번에 이동할 수 있되, 3칸 연속만 불가능.
dp = [0] * (10000 + 1)
dp[0] = g[0]
dp[1] = g[0] + g[1]
dp[2] = max(g[0], g[1]) + g[2]

result = 0
for i in range(3, n + 1):
    dp[i] = max(dp[i - 3] + g[i - 1], dp[i - 2]) + g[i]

print(dp[n - 1])
