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
s = list(map(str, input().strip()))

# print(s)

ans = []

def move(target):
    init = True
    tmp = 0
    for i in s:

        # 앞에 있는거 지나치기
        if init and i == target:
            continue

        # 이후부터는
        elif init and i != target:
            init = False

        elif (not init) and i == target:
            tmp += 1
    return tmp

def moveback(target):
    init = True
    tmp = 0
    for i in reversed(s):

        # 앞에 있는거 지나치기
        if init and i == target:
            continue

        # 이후부터는
        elif init and i != target:
            init = False

        elif (not init) and i == target:
            tmp += 1
    return tmp


# R, B 앞으로
ans.append(move('B'))
ans.append(move('R'))
ans.append(moveback('B'))
ans.append(moveback('R'))

print(min(ans))











