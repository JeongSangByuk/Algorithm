import math
import sys
from collections import deque
import itertools
import heapq
from bisect import bisect_left

# sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

t = int(input())

command = ['D','S','L','R']


def D_count(a):
    return (2 * a) % 10000 if 2 * a >= 10000 else 2 * a

def S_count(a):
    return 9999 if a == 0 else a - 1

def LR_count(a, isL):

    # 1,2,3,4
    # 2,3,4,1
    # 4,1,2,3
    # 0,1,2,3
    # 1,0,0,0

    k1 = a // 1000
    k2 = (a % 1000) // 100
    k3 = (a % 100) // 10
    k4 = (a % 10)

    if isL:
        return k2 * 1000 + k3 * 100 + k4 * 10 + k1
    else:
        return k4 * 1000 + k1 * 100 + k2 * 10 + k3

def bfs(a, b):
    que = deque()
    que.append((a, ""))
    visited = set()
    visited.add(a)

    while que:
        # print(que)
        node, s = que.popleft()

        l = [D_count(node), S_count(node), LR_count(node,True), LR_count(node,False)]

        for i, v in enumerate(l):
            if v not in visited:

                if v == b:
                    return s + command[i]

                que.append((v, s + command[i]))
                visited.add(v)

def sol():
    a, b = map(int, input().split())

    print(bfs(a, b))

for i in range(t):
    sol()
