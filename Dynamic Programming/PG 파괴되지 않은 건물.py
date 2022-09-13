import copy
import sys
import math
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def solution(board, skill):

    answer = 0
    n = len(board)
    m = len(board[0])

    tmp_board = [[0] * (m + 1) for _ in range(n + 1)]

    for s in skill:
        t, r1, c1, r2, c2, degree = s
        tmp_board[r1][c1] += degree if t == 2 else -degree
        tmp_board[r1][c2 + 1] += -degree if t == 2 else degree
        tmp_board[r2 + 1][c1] += -degree if t == 2 else degree
        tmp_board[r2 + 1][c2 + 1] += degree if t == 2 else -degree

    # 행 기준 누적합
    for i in range(n):
        for j in range(m):
            tmp_board[i][j+1] += tmp_board[i][j]

    # 열 기준 누적합
    for i in range(n):
        for j in range(m):
            tmp_board[i + 1][j] += tmp_board[i][j]

    for i in range(0,n):
        for j in range(0,m):

            board[i][j] += tmp_board[i][j]

            if board[i][j] > 0:
                answer+=1

    #print(board)
    #print(answer)
    return answer

board = eval(input())
skill = eval(input())
print(solution(board,skill))





