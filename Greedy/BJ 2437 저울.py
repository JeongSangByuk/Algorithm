import sys
from collections import deque
import itertools
import heapq

# https://aerocode.net/392

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
g = list(map(int, input().split()))
g.sort()

result = 1

for i in g:
    if result < i:
        break
    result += i

print(result)