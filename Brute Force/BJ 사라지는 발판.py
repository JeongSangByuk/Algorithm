import copy
import sys
import math
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

dy, dx = [-1,1,0,0], [0,0,-1,1]

# 실패 풀이
def solution2(board, aloc, bloc):
    answer = []
    n = len(board)
    m = len(board[0])

    que = deque()

    a = aloc
    b = bloc
    visited = set()

    que.append(((a[0],a[1]),(b[0],b[1]),visited,0))

    # visited.add(a)
    # visited.add(b)

    while que:

        a,b,visited,moveCnt = que.popleft()
        #print(a,b,visited,moveCnt)
        tmpMoveCnt = moveCnt
        isAMoved = False

        # a 선이동
        for i in range(4):

            nay = a[0] + dy[i]
            nax = a[1] + dx[i]
            tmpMoveCnt = moveCnt
            isBMoved = False

            if 0 <= nay < n and 0 <= nax < m and  board[nay][nax] == 1 and (nay,nax) not in visited:
                isAMoved = True
                tmpMoveCnt += 1

                tmp_visited = visited.copy()
                tmp_visited.add((a[0], a[1]))

                if (b[0],b[1]) in tmp_visited:
                    answer.append(tmpMoveCnt)
                    break

                # b 이동
                for j in range(4):

                    nby = b[0] + dy[j]
                    nbx = b[1] + dx[j]

                    if  0 <= nby < n and 0 <= nbx < m  and board[nby][nbx] == 1 and (nby, nbx) not in tmp_visited:

                        isBMoved = True
                        tmpMoveCnt += 1

                        # 발판 사라지기
                        tmp_visited.add((b[0], b[1]))

                        que.append(((nay, nax),(nby, nbx), tmp_visited, tmpMoveCnt))

        if ((not isAMoved) and (not isBMoved)) :
            answer.append(tmpMoveCnt)
            #print(answer)
            #answer = min(answer,tmpMoveCnt)

    return min(answer)

dir = ((-1,0),(0,1),(1,0),(0,-1))


# https://sujeng97.tistory.com/36
def A_turn(ar,ac,br,bc,cnt,board):

    if board[ar][ac] == 0:
        return (1, cnt)

    winner = []
    loser = []
    flag = False

    for dr,dc in dir:
        nr,nc = ar+dr,ac+dc
        if 0<=nr<len(board) and 0<=nc<len(board[0]) and board[nr][nc] == 1:

            flag = True
            temp = [row[:] for row in board]
            temp[ar][ac] = 0

            iswin, turn = B_turn(br,bc,nr,nc,cnt+1,temp)

            if iswin:
                winner.append(turn)
            else:
                loser.append(turn)

    if flag:
        if winner:
            return (0,min(winner))
        else:
            return (1,max(loser))
    else:
        return (1,cnt)

def B_turn(br,bc,ar,ac,cnt,board):

    if board[br][bc] == 0:
        return (1,cnt)

    winner = []
    loser = []
    flag = False

    for dr,dc in dir:

        nr,nc = br+dr,bc+dc

        if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == 1:
            flag = True
            temp = [row[:] for row in board]
            temp[br][bc] = 0

            iswin,turn = A_turn(ar,ac,nr,nc,cnt+1,temp)
            if iswin:
                winner.append(turn)
            else:
                loser.append(turn)

    if flag:
        if winner:
            return (0,min(winner))
        else:
            return (1,max(loser))
    else:
        return (1,cnt)


def solution(board, aloc, bloc):
    ar,ac,br,bc = aloc[0],aloc[1],bloc[0],bloc[1]
    answer = A_turn(ar,ac,br,bc,0,board)[1]
    return answer


board = eval(input())
aloc = eval(input())
bloc= eval(input())

print(solution(board, aloc, bloc))



