import sys
from collections import deque
import itertools
import heapq

# https://aerocode.net/392

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())
g = list(map(int, input().split()))
g.sort()

now = 0
answer = 0
m -= 1

for i in range(len(g)):

    if now < g[i]:
        now = g[i] + m
        answer += 1

print(answer)