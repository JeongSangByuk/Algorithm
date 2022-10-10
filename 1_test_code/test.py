import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline

a = [-10, -10, 2, 3, 3, 6, 7, 10, 10, 10]

dic = defaultdict(int)
for i in a:
    dic[i] += 1

print(dic)

a = list(set(a))
a.sort()

print(a)