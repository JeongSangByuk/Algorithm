import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

k = int(input())

for kk in range(k):
    n, m = map(int, input().split())

    ans = 1
    ans2 = 1

    cnt = 0
    tmp = m
    while cnt != n:
        ans *= tmp
        tmp -= 1
        cnt += 1

    for i in range(n,0,-1):
        ans2 *= i

    print(ans//ans2)