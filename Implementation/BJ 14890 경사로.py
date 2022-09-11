import copy
import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, l = map(int, input().split())

g = [list(map(int, input().split())) for _ in range(n)]

answer = 0

def isCorrect(r, i,value,k,visited):


    tmp_l = 0
    ori_i = i
    while True:

        if not(0 <= i < n):
            return False


        if r[i] == value and visited[i] == False:
            tmp_l += 1
            i += k

        else:
            return False

        if tmp_l == l:

            for j in range(tmp_l):
                visited[ori_i + (k * j)] = True

            return True



def move(r):
    global answer
    rl = len(r)

    visited = [False] * n

    for i in range(0, rl - 1):

        # pass
        if r[i+1] == r[i]:
            continue

        # 높이 차이 1이상, 못 지나감
        elif abs(r[i+1] - r[i]) > 1:
            return

        # 하나 차이
        elif abs(r[i+1] - r[i]) == 1:

            isCorrected = False

            # decrease
            if r[i+1] < r[i]:
                isCorrected = isCorrect(r,i+1, r[i+1], 1,visited)


            # increase
            else:
                isCorrected = isCorrect(r,i, r[i], -1,visited)

            if not isCorrected:
                return

    answer += 1
    #print(r,visited)


for i in range(n):
    move(g[i])

for i in range(n):
    c = [g[j][i] for j in range(n)]
    move(c)

print(answer)












