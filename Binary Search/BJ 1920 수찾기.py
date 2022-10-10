import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline

n = int(input())

g = list(map(int, input().split()))

m = int(input())

g2 = list(map(int, input().split()))

g.sort()

def search(target):

    start = 0
    end = n - 1

    while start <= end:

        mid = (start + end) // 2

        if g[mid] == target:
            return 1
        elif g[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return 0


for i in g2:
    print(search(i))






