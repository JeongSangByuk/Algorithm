
import sys
from collections import deque, defaultdict

input = sys.stdin.readline

n = int(input())

lope = []

for i in range(n):
    lope.append(int(input().strip()))

lope.sort()

answer = 0

for i in range(n):
    if answer < lope[i] * (n-i):
        answer = lope[i] * (n-i)

print(answer)
