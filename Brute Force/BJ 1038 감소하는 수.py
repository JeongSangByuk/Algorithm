import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())

g = [str(i) for i in range(10)]

total = 0
ans = -1

for i in range(1, 11):

    l = list(itertools.combinations(g, i))

    tmp = total
    total += len(l)

    if n < total:

        t = []
        for j in l:
            p = int(''.join(reversed(list(j))))

            t.append(p)

        t.sort()
        ans = (t[n - tmp])
        break

    tmp = total

if ans != -1:
    print(ans)
else:
    print(-1)
    
