import copy
import sys
from collections import deque
from _collections import defaultdict
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

d = [2,3]

d2 = [4,5]

l = d + d2

heapq.heapify(l)

print(l)


