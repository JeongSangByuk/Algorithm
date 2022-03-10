import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

s = input().strip()
s1 = input().strip()

answer = 0

l = len(s1)

i = 0
while i <= len(s) - l:

    if s[i:i+l] == s1:
        answer += 1
        i += l
    else:
        i += 1

print(answer)