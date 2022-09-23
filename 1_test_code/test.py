import copy
import sys
from collections import deque
from _collections import defaultdict
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

v = set()
q = deque()
q.append(1)

v.add(tuple(q))

print(v)

