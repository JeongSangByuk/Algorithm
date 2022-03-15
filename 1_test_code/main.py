import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
<<<<<<< HEAD

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
=======

arr = [int(input()) for _ in range(n)] + [0]

# n이 1인 경우 때문에,
dp = [0] * (n + 2)

dp[1] = arr[0]
dp[2] = arr[1] + arr[0]

for i in range(3, n + 1):
    dp[i] = max(dp[i - 2], arr[i - 2] + dp[i - 3]) + arr[i - 1]

print(arr)
print(dp)
print(dp[n])
>>>>>>> bea72d0f09b9831d799c36d927363004758a3166
