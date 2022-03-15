import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
arr = [[0] for _ in range(n + 1)]

arr[0] = 1
arr[1] = 2

for i in range(2,n + 1):
    arr[i] = arr[i-2] + arr[i-1]

print(arr)