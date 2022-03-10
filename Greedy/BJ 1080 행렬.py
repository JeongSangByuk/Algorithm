import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(str,input().strip())) for _ in range(n)]
b = [list(map(str,input().strip())) for _ in range(n)]

answer = 0

def change(y,x):

    for i in range(3):
        for j in range(3):
            if a[y + i][x + j] == '1':
                a[y + i][x + j] = '0'
            else:
                a[y + i][x + j] = '1'

for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] != b[i][j]:
            change(i,j)
            answer += 1

is_same = True

for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            is_same = False

if is_same:
    print(answer)
else:
    print(-1)