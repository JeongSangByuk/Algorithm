import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)

input = sys.stdin.readline

l, c = map(int, input().split())

alpha = list(map(str, input().split()))

alpha.sort()

alpha = list(itertools.combinations(alpha,l))

result = []

for i in alpha:

    m_cnt = 0
    j_cnt = 0

    for j in i:
        if j in ['a','i','e','o','u']:
            m_cnt += 1
        else:
            j_cnt += 1


    if m_cnt >= 1 and j_cnt >= 2:
        result.append("".join(i))

print(*result, sep='\n')





