import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline

a = set()

a.add(1)
a.add(2)
a.add(3)
b = a.copy()
for i in a:
    print(i)
b.pop()

print(a)
a.add(b)
print(a)