import sys
from collections import deque

input = sys.stdin.readline

def solution(m, n, puddles):
    answer = 0

    g = [[0]*m for _ in range(n)]

    for p in puddles:
        # 물 웅덩이를 -1로
        g[p[1] - 1][p[0] - 1] = -1

    for i in range(n):
        for j in range(m):

            # 물웅덩이
            if g[i][j] == -1:
                continue

            # 0,0 일 경우
            if i == 0 and j == 0 :
                continue

            if i == 0:

                # 전에게 물웅덩이 일경우
                if g[i][j - 1] == -1:
                    g[i][j] = -1
                else:
                    g[i][j] = 1
                continue

            if j == 0:

                # 전에게 물웅덩이 일경우
                if g[i - 1][j] == -1:
                    g[i][j] = -1
                else:
                    g[i][j] = 1
                continue

            # 최단 경로의 수 더하기
            n1, n2 = 0, 0

            # 위에게 물웅덩이가 아닐때만
            if g[i-1][j] != -1:
                n1 = g[i-1][j]

            # 왼쪽이 물웅덩이가 아닐때만
            if g[i][j - 1] != -1:
                n2 = g[i][j - 1]

            # 둘다 0이면 못옴 ㅅㄱ
            if n1 == 0 and n2 == 0:
                g[i][j] = -1
            else:
                # 최단 경로수 더하기
                g[i][j] = n1 + n2

    print(g)

    # 못도달하면 경우의 수 0
    if g[n-1][m-1] == -1:
        g[n - 1][m - 1] = 0

    return g[n-1][m-1] % 1000000007

m = int(input())
n = int(input())
puddles = eval(input())

print(solution(m, n, puddles))
