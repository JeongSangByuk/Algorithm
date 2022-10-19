import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline

l = [1,2,3,4]

l2 = [1,2]

print(list(set(l) - set(l2)))