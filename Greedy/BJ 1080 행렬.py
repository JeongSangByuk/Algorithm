import sys
from collections import deque
import itertools
import heapq

# 왜 최적해인가?
# https://www.acmicpc.net/board/view/13509
# 문제의 목적은 행렬 A를 행렬 B로 바꾸는 것. 결국 A와 B에서 다른 부분은 반드시 한번 flip해줘야 한다.
# 여기서 최적해가 되려면 반드시 한 번만 뒤집는 것이 옳다! (3,5번 flip하면 결과는 똑같아지기 때문)
# 때문에 최적해를 구하기 위해서는 바꿀 필요가 있는 부분은 flip하고,
# 바꿀 필요 없는 부분은 확정하고 넘어가면 된다.
# 이것이 그리디하게 최소로 flip하는 방법.

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(str,input().strip())) for _ in range(n)]
b = [list(map(str,input().strip())) for _ in range(n)]

answer = 0

def change(y,x):

    for i in range(3):
        for j in range(3):
            if a[y + i][x + j] == '1':
                a[y + i][x + j] = '0'
            else:
                a[y + i][x + j] = '1'

for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] != b[i][j]:
            change(i,j)
            answer += 1

is_same = True

for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            is_same = False

if is_same:
    print(answer)
else:
    print(-1)