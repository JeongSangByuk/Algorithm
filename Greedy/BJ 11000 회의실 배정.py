import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())

g = [list(map(int, input().split())) for _ in range(n)]
g.sort(key=lambda x:(x[0],x[1]))
#print(g)

stack = []
heapq.heappush(stack, g[0][1])

for i in range(1, n):

    is_added = False

    if stack[0] > g[i][0]:
        heapq.heappush(stack, g[i][1])

    else:
       k = heapq.heappop(stack)
       heapq.heappush(stack, g[i][1])

print(len(stack))