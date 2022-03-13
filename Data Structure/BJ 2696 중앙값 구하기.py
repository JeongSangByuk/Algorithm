import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())

result = []
for nn in range(n):
    k = int(input())

    cnt = 0
    answer = [[]]
    answer_cnt = 0
    left, right = [], []
    mid = 0

    g = []

    for i in range((k//10) + 1):
        g += list(map(int, input().split()))

    for i in range(k):

        if i == 0:
            mid = g[i]
            answer[cnt].append(mid)
            answer_cnt += 1
            continue

        if mid <= g[i]:
            heapq.heappush(right, g[i])
        else:
            heapq.heappush(left, -g[i])

        if i % 2 == 0:

            if len(left) < len(right):
                tmp = mid
                mid = heapq.heappop(right)
                heapq.heappush(left, -tmp)

            elif len(left) > len(right):
                tmp = mid
                mid = -1 * heapq.heappop(left)
                heapq.heappush(right, tmp)

            answer[cnt].append(mid)
            answer_cnt += 1
            if len(answer[cnt]) == 10:
                cnt += 1

                answer.append([])

    result.append(answer_cnt)
    for i in answer:
        result.append(' '.join(list(map(str,i))))


print(*result, sep='\n')
