import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
gp, gn, gz = [],[],[]

for i in range(n):

    k = int(input())

    if k > 0 :
        gp.append(k)
    elif k == 0:
        gz.append(k)
    else:
        gn.append(k)

gp.sort()
gn.sort(reverse=True)

answer = 0

while gp:

    t1 = gp.pop()

    if gp:
        t2 = gp.pop()

        if t1 > 1 and t2 > 1:
            answer += t1*t2
        else:
            answer += (t1 + t2)

    else:
        answer += t1

while gn:

    t1 = gn.pop()

    if gn:
        t2 = gn.pop()
        answer += t1*t2

    else:
        if not gz:
            answer += t1

print(answer)















