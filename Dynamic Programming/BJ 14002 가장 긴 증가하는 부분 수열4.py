import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline

n = int(input())
g = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if g[i] > g[j]:
            dp[i] = max(dp[i], dp[j] + 1)

a1 = max(dp)
a2 = []

tmp = a1
for i in range(n-1, -1, -1):

    if dp[i] == tmp:
        a2.append(g[i])
        tmp -= 1

print(a1)
a2.reverse()
print(*a2, sep=' ')





















