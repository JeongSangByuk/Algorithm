import sys
import heapq
from collections import deque, defaultdict
import itertools

sys.setrecursionlimit(10**7)

input = sys.stdin.readline

MAX = 100000

n, k = map(int, input().split())

def bfs():

    que = deque()
    que.append((n,0))
    v = set()

    while que:

        node,cnt = que.popleft()

        if node == k:
            print(cnt)
            break

        for j in (node - 1, node + 1, node * 2):

            if 0 <= j <= MAX and j not in v:
                v.add(j)
                que.append((j,cnt + 1))

bfs()