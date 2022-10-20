import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline

dic = dict()

dic[(1,2)] = 1

dic[(2,2)] = 2

for i in dic:
    print(i)
    dic[i] = 3

print(dic)

print(list(dic.values()))