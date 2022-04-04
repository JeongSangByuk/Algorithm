import sys
from collections import deque
import itertools
import heapq

n, m = map(int, input().split())
g = [list(input().strip()) for _ in range(n)]

ans1 = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
ans2 = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']


def change(tg):
    cnt = 0
    cnt2 = 0
    # print(tg)
    for i in range(8):
        for j in range(8):

            if i % 2 == 0:
                if tg[i][j] != ans1[j]:
                    cnt += 1
            else:
                if tg[i][j] != ans2[j]:
                    cnt += 1

    for i in range(8):
        for j in range(8):

            if i % 2 == 0:
                if tg[i][j] != ans2[j]:
                    cnt2 += 1
            else:
                if tg[i][j] != ans1[j]:
                    cnt2 += 1

    return min(cnt,cnt2)

ans = 100
for i in range(n-7):
    for j in range(m - 7):
        ans = min(ans,change([g[item][j:j+8] for item in range(i,i+8)]))

print(ans)

