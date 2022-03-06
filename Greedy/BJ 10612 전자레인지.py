import sys
from collections import deque, defaultdict

input = sys.stdin.readline

n = int(input())

time = [300, 60, 10]

def solution(n):

    answer = [0, 0, 0]

    i = 0

    while True:

        if n == 0:
            print(answer[0], answer[1], answer[2])
            return 0

        if i >= 3 and n != 0:
            print("-1")
            return 0

        if n // time[i] == 0:
            answer[i] = 0
            i += 1
            continue

        answer[i] = n//time[i]
        n = n - time[i] * (n//time[i])
        i += 1

solution(n)
