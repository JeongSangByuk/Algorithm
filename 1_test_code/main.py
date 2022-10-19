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
people = list(map(int, input().split()))
p = [list(map(int, input().split())) for _ in range(n)]

dic = dict()

for i in range(1,n+1):
    dic[i] = []

for i in range(n):

    for j in p[i][1:]:

        if (i + 1) not in dic[j]:
            dic[j].append(i+1)
        if j not in dic[i + 1]:
            dic[i+1].append(j)

def count(s):
    tmp = 0
    for i in s:
        tmp += people[i-1]
    return tmp

def is_connect(a, b):

    visited = set()
    que = deque()

    t = a[0]

    que.append(t)
    visited.add(t)
    result = 0

    while que:

        result += 1
        node = que.popleft()

        for i in dic[node]:

            if i not in visited and i not in b and i in a:
                que.append(i)
                visited.add(i)

    if result == len(a):
        return True

    return False



base = {i for i in range(1, n + 1)}
ans = []

for i in range(1, n//2 + 1):

    l = list(itertools.combinations(base, i))

    for a in l:
        a = set(a)
        b = base - a

        #print(a,b)

        if is_connect(list(a), list(b)) and is_connect(list(b),list(a)):
            ans.append(abs(count(a) - count(b)))


if ans:
    print(min(ans))
else:
    print(-1)








