import copy
import sys
from collections import deque
from _collections import defaultdict
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

v = [[1,[]] for i in range (10)]
v[0][1].append(2)
v[3][1].append(2)

a = v[3][1][:]
a.append(4)

v[3][1] = a[:]

print(v)
print(a)





