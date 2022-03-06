import sys
from collections import deque

input = sys.stdin.readline

def solution(triangle):


    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):

            #  가장 자리부터 채운다
            if j == 0 :
                triangle[i][0] += triangle[i-1][0]

            elif j == i :
                triangle[i][i] += triangle[i - 1][i - 1]

            else:
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])

    return max(triangle[len(triangle) - 1])

triangle = eval(input())

print(solution(triangle))
