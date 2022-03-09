import sys
from collections import deque
import itertools

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

answer = []

while True:
    l, p, v = map(int, input().split())

    if l <= 0:
        break

    t_a = 0

    t = v//p
    t2 = (v-p*t)
    if (v-p*t) >= l:
        t2 = l

    t_a += l * t + t2
    answer.append(t_a)

for i in range(len(answer)):
    print('Case %d: %d' %((i+1), answer[i]))



