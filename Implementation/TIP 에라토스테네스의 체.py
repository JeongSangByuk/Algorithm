import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline

n = 4000000
prime = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if prime[i] == True:

        j = 2

        while i * j <= n:
            prime[i * j] = False
            j += 1
