import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

arr = [1,2,3,4]

for i in enumerate(arr):
    i[1] = 3

print(arr)