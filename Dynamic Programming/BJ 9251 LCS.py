import sys
from collections import deque
import itertools
import heapq

# https://myjamong.tistory.com/317

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

str1 = list(input().strip())
str2 = list(input().strip())

# 풀이 1

# dp = [[0] * (len(str2) + 1) for _ in range((len(str1) + 1))]
#
# for i in range(1, len(str1) + 1):
#     for j in range(1, len(str2) + 1):
#
#         if str1[i - 1] == str2[j - 1]:
#             dp[i][j] = dp[i - 1][j - 1] + 1
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#
# print(dp[-1][-1])

#######################

# 풀이2

dp = [0] * len(str2)

for i in range(len(str1)):
    cnt = 0

    for j in range(len(str2)):
        if cnt < dp[j]:
            cnt = dp[j]
        elif str1[i] == str2[j]:
            dp[j] = cnt + 1

print(max(dp))
    




