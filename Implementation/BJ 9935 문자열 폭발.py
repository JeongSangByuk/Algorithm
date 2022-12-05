import sys
from collections import deque
import itertools
import heapq
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

a = list(input().strip())
b = str(input().strip())

stack = []
l = len(b)

for i in range(len(a)):
    stack.append(a[i])

    if ''.join(stack[-l:]) == b:
        for _ in range(l):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
