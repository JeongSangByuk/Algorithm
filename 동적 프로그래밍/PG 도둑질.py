import sys
from collections import deque

input = sys.stdin.readline

def solution(money):

    # 첫번째 집을 털었을 경우
    # i번째 집까지 털었을 때의 최댓값 배열
    max_money = [0] * len(money)

    max_money[0] = money[0]
    max_money[1] = money[0]

    for i in range(2 , len(money) - 1):

        # i-1의 집을 털었을 경우와 그렇지 않을 경우 중 큰 값.
        max_money[i] = max(max_money[i-1], max_money[i-2] + money[i])

    a1 = max(max_money)

    # 첫 번째 집을 털지 않았을 경우
    max_money = [0] * len(money)

    max_money[1] = money[1]

    for i in range(2, len(money)):
        # i-1의 집을 털었을 경우와 그렇지 않을 경우 중 큰 값.
        max_money[i] = max(max_money[i - 1], max_money[i - 2] + money[i])

    a2 = max(max_money)

    return max(a1,a2)

money = eval(input())

print(solution(money))
