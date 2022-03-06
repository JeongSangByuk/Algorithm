
import sys
from collections import deque, defaultdict

input = sys.stdin.readline

n = int(input())

def answer():

    k5 = n // 5

    while True:

        k3 = (n - k5 * 5) % 3

        if k5 == 0 and k3 != 0:
            return -1

        if k3 == 0:
            return k5 + (n - k5 * 5) // 3
        else:
            k5 -= 1

print(answer())
