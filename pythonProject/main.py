
global n, board, answer

def updateBoard(x, y):

    # 업데이트 했으면 True를 반환
    if x >= n or y >= n :
        return False

    if board[y][x] == 1:
        return False

    if board[y][x] != 1:

        # 가로세로 다 1로
        for i in range(0, n):
            board[y][i] = 1
            board[i][x] = 1

        # 대각선 범위 1로
        minX = x
        minY = y

        maxX = x
        maxY = y

        # 바꿀 대각선 범위를 구한다
        while minX != 0 and minY != 0:
            minY -= 1
            minX -= 1

        while maxX != 0 and maxY != n - 1:
            maxY += 1
            maxX -= 1

        # 대각선 범위를 다 1로 바꾼다.
        while minX < n and minY < n:
            board[minY][minX] = 1
            minX += 1
            minY += 1

        while maxX < n and maxY >= 0:
            board[maxY][maxX] = 1
            maxX += 1
            maxY -= 1

        return True

def initBoard():
    for i in range(len(board)):
        for j in range(len(board)):
            board[i][j] = 0

def doProcess(x,y):

    cnt = 0

    for i in range(y,n):
        for j in range(x, n):
            if updateBoard(i, j):
                cnt += 1
    if cnt >= n :
        answer += 1

answer = 0

n = int(input())

board = [[0 for _ in range(n)] for _ in range(n)]

for i in range(len(board)):
    for j in range(len(board)):
        doProcess(i, j)
        initBoard()

print(answer)



# for i in range(len(board)):
#     print(board[i])
