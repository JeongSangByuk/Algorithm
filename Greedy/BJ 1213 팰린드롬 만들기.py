import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

s = list(input().strip())

s.sort()

dic = {}

for i in range(len(s)):
    if s[i] not in dic:
        dic[s[i]] = 1
    else:
        dic[s[i]] += 1

l = []

for i in dic.items():
    l.append([i[0],i[1]])


def solution():

    ans = ""
    odd_c = ""
    odd_cnt = 0

    for i in range(len(l)):

        # 홀수인게 하나 이상 있으면 못만든다.
        if l[i][1] % 2 != 0:
            odd_cnt += 1
            # l[i][1] -= 1
            odd_c = l[i][0]

        if odd_cnt > 1:
            return "I'm Sorry Hansoo"

    for i in range(len(l)):
        ans += (l[i][0] * (l[i][1]//2))

    return ans + odd_c + ans[::-1]

print(solution())
