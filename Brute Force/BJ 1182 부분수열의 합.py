import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)

input = sys.stdin.readline

n, s = map(int, input().split())

numbers = list(map(int, input().split()))

seq = []

for i in range(1, n + 1):
    seq.extend(list(itertools.combinations(numbers,i)))

result = 0

for i in seq:

    if sum(i) == s:
        result += 1

print(result)




