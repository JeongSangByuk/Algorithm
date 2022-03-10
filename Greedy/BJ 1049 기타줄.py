import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())

brand = [tuple(map(int, input().split())) for _ in range(m)]
brand2 = brand[:]

brand.sort()
brand2.sort(key = lambda x:x[1])

answer = 0

# case1 다 패키지
if n % 6 == 0:
    answer = brand[0][0] * n//6
else:
    answer = brand[0][0] * (n//6 + 1)

# case2 다 낱개
answer = min(answer, brand2[0][1] * n)

# case3 패키지 + 낱개
tmp = brand[0][0] * (n//6) + brand2[0][1] * (n % 6)
answer = min(answer, tmp)

print(answer)





