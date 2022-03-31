import sys
from collections import deque
import itertools
import heapq

n = int(input())
g = list(map(int, input().split()))
c = list(map(int, input().split()))

ans = []

def cal(j,num,cc):


    if j == n:
        ans.append(num)
        return

    for i in range(4):

        if cc[i] > 0:
            tmp_c = cc[:]
            tmp_c[i] -= 1

            if i == 0:
                cal(j + 1, num + g[j], tmp_c)

            elif i == 1:
                cal(j + 1, num - g[j], tmp_c)

            elif i == 2:
                cal(j + 1, num * g[j], tmp_c)

            elif i == 3:
                r = num // g[j]
                if (num < 0 and g[j] > 0) or (num > 0 and g[j] < 0):
                    num *= -1
                    r = num//g[j]
                    r *= -1
                cal(j + 1, r, tmp_c)

cal(1, g[0],c)

#print(ans)
print(max(ans))
print(min(ans))






