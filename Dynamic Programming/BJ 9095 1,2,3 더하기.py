import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())

ans = [1,2,4]
for i in range(3, 10):
    ans.append(ans[i-3] + ans[i-2] + ans[i-1])

for i in range(n):
    k = int(input())
    print(ans[k-1])



