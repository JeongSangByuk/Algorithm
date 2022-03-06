
import sys
from collections import deque, defaultdict

input = sys.stdin.readline

n, k = map(int, input().split())

money = []

for i in range(n):
    money.append(int(input().strip()))

def solution(k) :

    answer = 0
    end = len(money) - 1

    # 결국 무조건 나눠지기 때문에
    while True:

        # 나눠지지 않으면 다음 동전으로
        if k // money[end] == 0 :
            end -= 1
            continue

        value = (k//money[end])
        answer += value
        k -= money[end] * (value)

        if k <= 0:
            return answer

print(solution(k))
