import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline

a = set()
b= set()
a.add((1,2))
b.add((1,2,3))
b.add((2,3))
a.update(b)

print(a)
print(b)

a.difference_update(b)

print(a)
print(b)