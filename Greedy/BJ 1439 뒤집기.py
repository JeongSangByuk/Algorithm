import sys
from collections import deque
import itertools

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

s = input().strip()

dic = {}
dic['0'] = 0
dic['1'] = 0

now = s[0]
dic[now] += 1

for i in range(len(s)):

    if now != s[i]:
        now = s[i]
        dic[s[i]] += 1

print(min(dic['0'],dic['1']))



