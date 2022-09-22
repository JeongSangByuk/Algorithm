import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

# https://velog.io/@leejy1373/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-DP-%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8-%EA%B3%B5%EB%B6%80Python
def solution(alp, cop, problems):

    max_alp = 0
    max_cop = 0

    for i in problems:
        max_alp = max(max_alp, i[0])
        max_cop = max(max_cop, i[1])

    # 최대값 보다 초기값이 낮을 수 있다.
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)

    INF = float('inf')

    dp = defaultdict(int)

    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            dp[(i,j)] = INF

    dp[(alp,cop)] = 0

    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):

            # 범위 제한
            if i + 1 <= max_alp:
                dp[(i + 1,j)] = min(dp[(i+1,j)], dp[(i,j)] + 1)

            # 범위 제한
            if j + 1 <= max_cop:
                dp[(i, j + 1)] = min(dp[(i, j + 1)], dp[(i, j)] + 1)

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:

                if i >= alp_req and j >= cop_req:

                    # 최대 값을 넘지 않아야 하기 때문에,
                    next_alp = min(max_alp, i + alp_rwd)
                    next_cop = min(max_cop, j + cop_rwd)

                    dp[(next_alp,next_cop)] = min(dp[(next_alp,next_cop)], dp[(i,j)] + cost)

    return dp[(max_alp,max_cop)]

alp = int(input())
cop = int(input())
problems = eval(input())
print(solution(alp, cop, problems))








