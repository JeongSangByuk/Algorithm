import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())

def solution():
    if n == 1:
        return 1
    elif n == 2:
        if m > 6:
            return 4
        else:
            return ((m-1)//2 + 1)
    elif n >= 3:
        if m <= 6:
            return min(m,4)
        else:
            return m - 2

print(solution())


