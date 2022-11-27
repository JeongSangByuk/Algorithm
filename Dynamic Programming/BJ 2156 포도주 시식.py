import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())

g = list(int(input()) for _ in range(n)) + [0] * (10000 - n)


dp = [0] * 10000

# dp 배열 : 해당 포도주 index까지의 최댓값 -> 선택되지 않아도 된다.
# 계단 오르기 문제와의 차이점. -> 계단오르기는 반드시, 1칸 or 2칸만을 이동해야함.
# but, 포도주 문제 -> 여러칸을 한번에 이동할 수 있되, 3칸 연속만 불가능.
dp[0] = g[0]
dp[1] = g[0] + g[1]
dp[2] = max(g[0] + g[2], g[1] + g[2], dp[1])

for i in range(3, n):
    dp[i] = max(dp[i-2] + g[i], dp[i - 3] + g[i-1] + g[i], dp[i - 1])

print(max(dp))