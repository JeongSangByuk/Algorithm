import sys
from collections import deque
import itertools
import heapq


d = deque()

d.append(1)
d.append(2)
d.append(3)

print(list(itertools.islice(d,0,2)))

print(d)