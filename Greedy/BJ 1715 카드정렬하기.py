import sys
import heapq
from collections import deque, defaultdict
import itertools

input = sys.stdin.readline

n = int(input().strip())
arr = []

for i in range(n):
    arr.append(int(input().strip()))

if n == 1:
    print(0)

else:

    answer = []
    heapq.heapify(arr)

    while arr:
        #print(arr)
        #print(answer)
        a1 = heapq.heappop(arr)

        if not arr:
            break

        a2 = heapq.heappop(arr)
        answer.append(a1 + a2)
        heapq.heappush(arr,a1 + a2)

    print(sum(answer))


