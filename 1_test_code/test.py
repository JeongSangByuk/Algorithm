import copy
import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

a = set()

a.add(2)

b = a.copy()

b.add(3)

b.remove(2)

print(a)
print(b)


