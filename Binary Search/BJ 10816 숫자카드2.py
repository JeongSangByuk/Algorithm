import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline

n = int(input())
g = list(map(int, input().split()))

m = int(input())
g2 = list(map(int, input().split()))

dic = defaultdict(int)
for i in g:
    dic[i] += 1

g = list(set(g))
g.sort()

def search(target):

    start = 0
    end = len(g) - 1

    while start <= end:

        mid = (start + end) // 2

        if target == g[mid]:
            return True
        if target > g[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return False

answer = []

for i in g2:

    t = search(i)

    if t:
        answer.append(dic[i])
    else:
        answer.append(0)

print(*answer, sep=' ')









