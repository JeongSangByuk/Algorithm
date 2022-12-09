import math
import sys
from collections import deque
import itertools
import heapq
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, l = map(int, input().split())
g = []
for i in range(n):
    g.append(list(map(int,input().split())))
    g[-1][1] -= 1

g.sort()

end = 0
answer = 0

for i in g:
    # print(end,answer)

    # 이미 커버 된 경우
    if i[0] <= end and i[1] <= end:
        continue

    if i[0] <= end and i[1] > end:

        t = math.ceil(((i[1] - end) / l))

        end += (t * l)
        answer += t
        continue

    t = math.ceil(((i[1] - i[0] + 1) / l))
    end = i[0] + t * l - 1
    answer += t

print(answer)
