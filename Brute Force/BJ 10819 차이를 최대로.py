import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)

input = sys.stdin.readline

n = int(input())

numbers = list(map(int, input().split()))

l = list(itertools.permutations(numbers,n))

result = sys.maxsize * -1

for i in l:

    c = 0

    for j in range(1, n):

        a = abs(i[j-1] - i[j])
        c = c + a

    result = max(result,c)

print(result)




