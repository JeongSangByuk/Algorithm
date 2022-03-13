import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())

g = list(map(int, input().split()))
n = len(g)
g.sort()

s = []

visit = set()
ans = []
def dfs(start):

    if len(s) == m:
        t = ''.join(map(str,s))
        if t not in visit:
            visit.add(t)
            ans.append(t)
            #print(' '.join(map(str,s)))
        return

    for i in range(start, n):
        s.append(g[i])
        dfs(i)
        s.pop()

dfs(0)
ans.sort()
#print(ans)

for i in range(len(ans)):
    print(' '.join(ans[i]))

#print(visit)
