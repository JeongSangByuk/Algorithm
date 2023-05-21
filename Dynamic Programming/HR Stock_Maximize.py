import math
import sys
from collections import deque
from collections import defaultdict
import itertools
from heapq import heappop, heappush
from bisect import bisect_left

input = sys.stdin.readline

t = int(input().strip())

# 해커랭크
# https://www.hackerrank.com/challenges/stockmax/problem

def stockmax(prices):

    _max = 0
    result = 0
    for i in range(len(prices) - 1, -1, -1):
        if _max < prices[i]:
            _max = prices[i]
        result += _max - prices[i]

    return result

for t_itr in range(t):
    n = int(input().strip())

    prices = list(map(int, input().rstrip().split()))

    result = stockmax(prices)

    print(str(result))

