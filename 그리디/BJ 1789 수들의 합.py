import sys
from collections import deque, defaultdict
import itertools

input = sys.stdin.readline

n = int(input().strip())

i = 1

s = 0

while True:

    s += i

    if s > n:
        break
    i+=1

print(i - 1)




