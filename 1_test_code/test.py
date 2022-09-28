import copy
import sys
from collections import deque
from _collections import defaultdict
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

<<<<<<< HEAD
d = [2,3]

d2 = [4,5]

l = d + d2

heapq.heapify(l)

print(l)
=======
v = set()
q = deque()
q.append(1)

v.add(tuple(q))
>>>>>>> f46e9e51e88c17e2adc0cc6461436951a6d56390

print(v)

