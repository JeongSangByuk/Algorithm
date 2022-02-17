import sys
from collections import deque, defaultdict
import itertools

input = sys.stdin.readline

n = int(input().strip())
arr = []

for i in range(n):
    arr.append(input().strip())

arr.sort()
arr.sort(reverse=True ,key = lambda x: (len(x)))

print(arr)