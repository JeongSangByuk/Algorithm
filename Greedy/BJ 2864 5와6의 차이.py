import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(str,input().strip().split())
n = list(n)
m = list(m)

m1,m2 = 0,0

for i in range(len(n)):
    if n[i] == '5':
        n[i] = '6'
for i in range(len(m)):
    if m[i] == '5':
        m[i] = '6'

m2 = int(''.join(n)) + int(''.join(m))

for i in range(len(n)):
    if n[i] == '6':
        n[i] = '5'
for i in range(len(m)):
    if m[i] == '6':
        m[i] = '5'

m1 = int(''.join(n)) + int(''.join(m))

print(m1, m2)
