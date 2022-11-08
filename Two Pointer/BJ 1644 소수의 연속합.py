import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline

n = int(input())

prime = [True for i in range(n + 1)]

# 에라토스테네스의 채
for i in range(2, int(math.sqrt(n)) + 1):

    if prime[i] == True:

        j = 2

        while i * j <= n:
            prime[i * j] = False
            j += 1

arr = []
for i,v in enumerate(prime):
    if v == True:
        arr.append(i)

l = len(arr)
s = 0
end = 2
answer = 0

# 투포인터
for start in range(2, l):

    while end < l and s < n:
        s += arr[end]
        end += 1

    if s == n:
        answer += 1

    s -= arr[start]

print(answer)
















