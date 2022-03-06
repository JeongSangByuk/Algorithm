
# https://rebas.kr/761

# def check(x):
#
#     for i in range(x):
#         # 열이 같거나, 대각선일 경우(행 - 행 = 열 - 열)
#         if row[x] == row[i] or abs(row[x] - row[i]) == x - i :
#             return False
#     return True


def dfs(x):
    global result

    # x가 n이라는 것은 n번째 줄까지 다돌았다는 뜻. 즉 횟수 +1
    if x == n:
        result += 1
        return

    # 각 행에 퀸을 놓는다.
    # 0부터 n까지 옮겨가면서 적합한 곳 찾기
    for i in range(n):
        if not(a[i] or b[i + x] or c[x-i+n-1]):
            a[i] = b[x + i] = c[x-i+n-1] = True
            dfs(x + 1)
            a[i] = b[x + i] = c[x-i+n-1] = False

n = int(input())

# 세로, 대각선 두개의 각각 배열
a = [False]*n
b = [False]*(2*n-1)
c = [False]*(2*n-1)

result = 0
dfs(0)

print(result)