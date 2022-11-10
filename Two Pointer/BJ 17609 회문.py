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
g = list(input().strip() for _ in range(n))

def detect(s, i, l):
    if s[i] == s[l - i]:
        return True
    return False

def detect_palindrome(s):
    # print(s)
    l = len(s)
    b = True

    for j in range(l//2):

        if not detect(s, j, l - 1):
            b = False
            break
    return b

def detect_pseudo_palindrome(s):

    l = len(s)
    b = True

    for j in range(l//2):

        if detect(s, j, l - 1):
            continue

        # 한개 빼보기
        if not detect(s, j, l - 1):

            b = False

            if 0 <= l - j - 1 < l and 0 <= j + 1 < l and s[j + 1] == s[l - j - 1]:
                b = detect_palindrome(s[j + 1 : l - j])

            if not b and 0 <= l - j - 2 < l and 0 <= j < l and s[j] == s[l - j - 2]:
                b = detect_palindrome(s[j:l - j - 1])

            return b

    return b

for i in range(n):

    b = detect_palindrome(g[i])

    if b:
        print(0)
        continue

    if detect_pseudo_palindrome(g[i]):
        print(1)
    else:
        print(2)















