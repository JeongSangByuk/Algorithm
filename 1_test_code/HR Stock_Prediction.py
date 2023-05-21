import math
import sys
from collections import deque
from collections import defaultdict
import itertools
from heapq import heappop, heappush
from bisect import bisect_left

input = sys.stdin.readline

# https://github.com/JeongSangByuk/resource/blob/main/%EA%B7%B8%EB%A6%BC1.png

query = [3,1,8]
g = [5, 6, 8, 4, 9, 10, 8, 3, 6, 4]
n = len(g)

left = [-1] * n
right = [-1] * n

for i in range(1, n):

    j = i - 1

    if g[j] < g[i]:
        left[i] = j
        continue

    while True:
        j = left[j]

        if g[j] < g[i]:
            left[i] = j
            break

        if left[j] == -1:
            left[i] = -1
            break


for i in range(n - 2, -1, -1):

    j = i + 1

    if g[j] < g[i]:
        right[i] = j
        continue

    while True:
        j = right[j]

        if g[j] < g[i]:
            right[i] = j
            break

        if right[j] == -1:
            right[i] = -1
            break

print(left)
print(right)

for i in query:
    i -= 1

    if left[i] == -1 and right[i] == -1:
        print(-1)
        continue

    if left[i] == -1:
        print(right[i])
        continue
    elif right[i] == -1:
        print(left[i])
        continue

    a = abs(left[i] - i)
    b = abs(right[i] - i)

    if a == b:
        print(left[i])
    elif a < b:
        print(left[i])
    else:
        print(right[i])

