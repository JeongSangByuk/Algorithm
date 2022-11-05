import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
_max = 10**n


def check_prime(k):

    for i in range(2, int(math.sqrt(k)) + 1):

        if k % i == 0:
            return False
        
    return True


def dfs(k):

    if len(str(k)) == n:
        print(k)
        return

    for i in range(10):
        tmp = k * 10 + i

        if check_prime(tmp):
            dfs(tmp)

for i in [2,3,5,7]:
    dfs(i)



