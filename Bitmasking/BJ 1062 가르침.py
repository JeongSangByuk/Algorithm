import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, k = map(int, input().split())
g = []

default_a = ['a','n','t','i','c']
total = set()
s = []
al_dic = defaultdict(int)

# k가 5보다 작을 경우 만들 수 없다.
if k < 5:
    print(0)
    sys.exit()

for i in range(n):
    t = input()
    t = t[4:]
    t = t[:len(t) - 5]

    ts = set()
    for i in t:

        if i not in default_a:
            ts.add(i)

    total = total.union(ts)

    # word 배열에 각 문자의 비트마스킹 저장
    b = 0
    for ch in ts:
        b = b | (1 << (ord(ch) - ord('a')))

    s.append(b)

# print(s)
# print(total)

if len(total) < k - 5:
    k = len(total)
else:
    k = k - 5

c = list(itertools.combinations(total, k))

ans = 0

# for i in c:
#     i = set(i)
#     cnt = 0
#     for j in s:
#         tmp = j.difference(i)
#
#         if len(tmp) == 0:
#             cnt += 1
#
#     ans = max(ans, cnt)

for i in c:
    # i = set(i)
    cnt = 0
    learn = 0

    # 배운거에 대한 비트 마스킹
    for ch in i:
        learn = learn | (1 << (ord(ch) - ord('a')))

    for j in s:
        if j & learn == j:
            cnt+=1

    ans = max(ans,cnt)

print(ans)


