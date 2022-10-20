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

b = set()
b.add(3)
a.update(b)
print(a)
