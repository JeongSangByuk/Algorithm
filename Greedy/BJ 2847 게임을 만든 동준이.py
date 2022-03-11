import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

t = int(input())

g = [int(input()) for _ in range(t)]
answer = 0

for i in range(t-1, 0, -1):

    if g[i] <= g[i-1]:
        tmp = g[i-1]
        g[i-1] = g[i] - 1
        answer += (tmp - g[i-1])

print(answer)


