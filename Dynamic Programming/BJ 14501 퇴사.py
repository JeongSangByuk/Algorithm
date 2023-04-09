import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
g = list(list(map(int, input().split())) for _ in range(n))

# i번째까지 밖에 없을 때의 최댓값 배열
dp = [0 for _ in range(n + 1)]

# print(list(i[0] for i in g))

for i in range(n):

    dp[i] = max(dp[i], dp[i - 1])

    tmp = i + g[i][0]

    if tmp >= n + 1:
        continue

    dp[tmp] = max(dp[tmp], dp[i] + g[i][1])

print(max(dp))