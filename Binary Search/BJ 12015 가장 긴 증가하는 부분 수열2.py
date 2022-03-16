import sys
from collections import deque
import itertools
import heapq
from bisect import bisect_left

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
g = list(map(int, input().split()))
dp = [0]

for i in g:

    if dp[-1] < i:
        dp.append(i)

    else:
        left = 0
        right = len(dp)

        # 이분탐색으로 들어갈 인덱스를 찾는다.
        # 결국 길이를 구하는 것이기 때문에, dp 배열 자체에 값은 중요하지 않다.
        while left < right:
            mid = (left + right) // 2

            if dp[mid] < i:
                left = mid + 1
            else:
                right = mid

        dp[right] = i

#print(dp)
print(len(dp) - 1)