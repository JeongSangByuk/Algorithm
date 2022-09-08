import copy
import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m  = map(int, input().split())

g = [list(map(int, input().split())) for _ in range(n)]

# 브루트 포스, 노가다 코드
def solution():
    shape = [[] for _ in range(5)]

    shape[0].append([[0,0],[0,1],[0,2],[0,3]])
    shape[0].append([[0,0],[1,0],[2,0],[3,0]])

    shape[1].append([[0,0],[0,1],[1,0],[1,1]])

    shape[2].append([[0,0],[1,0],[2,0],[2,1]])
    shape[2].append([[0,0],[0,1],[0,2],[1,0]])
    shape[2].append([[0,0],[0,1],[1,1],[2,1]])
    shape[2].append([[1,0],[1,1],[1,2],[0,2]])

    shape[2].append([[2,0],[0,1],[1,1],[2,1]])
    shape[2].append([[0,0],[0,1],[0,2],[1,2]])
    shape[2].append([[0,0],[0,1],[1,0],[2,0]])
    shape[2].append([[0,0],[1,0],[1,1],[1,2]])

    shape[3].append([[0,0],[1,0],[1,1],[2,1]])
    shape[3].append([[1,0],[1,1],[0,1],[0,2]])
    shape[3].append([[0,1],[1,1],[1,0],[2,0]])
    shape[3].append([[0,0],[0,1],[1,1],[1,2]])

    shape[4].append([[0,0],[0,1],[0,2],[1,1]])
    shape[4].append([[0,1],[1,1],[2,1],[1,0]])
    shape[4].append([[0,1],[1,0],[1,1],[1,2]])
    shape[4].append([[0,0],[1,0],[2,0],[1,1]])

    def countValue(y,x,s,t):

        v = 0

        for k in range(4):
            pY = (y + s[t][k][0])
            pX = (x + s[t][k][1])

            if 0 <= pY < n and 0 <= pX < m:
                v += g[pY][pX]
            else:
                return -1

        return v

    def count(i):

        l =len(shape[i])
        s = shape[i]
        answer = 0

        for t in range(l):

            for y in range(n):
                for x in range(m):

                    v = countValue(y,x,s,t)

                    if v == -1:
                        continue

                    answer = max(answer,v)

        return answer

    answer = 0

    for i in range(5):
        answer = max(answer, count(i))

    print(answer)

# dfs 활용
# https://cijbest.tistory.com/87


maxValue = 0

def solution2():

    global maxValue

    dy, dx = [-1,1,0,0], [0,0,-1,1]
    moveOther = list(itertools.combinations([0, 1, 2, 3], 3))

    visited = [[-1] * m for _ in range(n)]

    # ㅗ, ㅜ, ㅓ, ㅏ 제외한 모양들 최대값 계산
    def dfs(y,x,dSum, cnt):

        global maxValue

        if cnt == 4:
            maxValue = max(maxValue,dSum)
            return

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == -1:

                visited[ny][nx] = 0
                dfs(ny,nx,dSum + g[ny][nx], cnt + 1)
                visited[ny][nx] = -1

    def count(y,x):
        global maxValue

        for i in range(4):
            tmp = g[y][x]

            for j in range(3):
                ny = y + dy[moveOther[i][j]]
                nx = x + dx[moveOther[i][j]]

                if not (0 <= ny < n and 0 <= nx < m):
                    tmp = 0
                    break
                tmp += g[ny][nx]

            maxValue = max(maxValue,tmp)

    for i in range(n):
        for j in range(m):
            visited[i][j] = 0
            dfs(i,j,g[i][j],1)
            visited[i][j] = -1
            count(i,j)

    print(maxValue)

# dfs 활용, 가지 치키, 로직 변경
# https://cijbest.tistory.com/87
def solution3():

    maxValue = 0

    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

    visited = [[-1] * m for _ in range(n)]

    maxValueInG = max(map(max, g))

    # ㅗ, ㅜ, ㅓ, ㅏ 제외한 모양들 최대값 계산
    def dfs(y, x, dSum, cnt):

        global maxValue

        # 가지 치기
        if maxValue >= dSum + maxValueInG * (4 - cnt):
            return

        if cnt == 4:
            maxValue = max(maxValue, dSum)
            return

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == -1:

                # ㅗ 모양
                if cnt == 2:
                    visited[ny][nx] = 0
                    dfs(y, x, dSum + g[ny][nx], cnt + 1)
                    visited[ny][nx] = -1

                visited[ny][nx] = 0
                dfs(ny, nx, dSum + g[ny][nx], cnt + 1)
                visited[ny][nx] = -1

    for i in range(n):
        for j in range(m):
            visited[i][j] = 0
            dfs(i, j, g[i][j], 1)
            visited[i][j] = -1

    print(maxValue)

solution2()
