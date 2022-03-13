import sys
from collections import deque
import itertools
import heapq

# visit 배열 관리 잘하자 좀 ^ㅡ^

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())

g = list(set(list(map(int, input().split()))))

g.sort()
n  = len(g)
s = []

visit = set()

def dfs(start):

    if len(s) == m:
        t = ' '.join(map(str,s))

        if t not in visit:
            visit.add(t)
            print(' '.join(map(str,s)))
        return

    for i in range(start, n):
        s.append(g[i])
        dfs(i)
        s.pop()

dfs(0)
#print(visit)
