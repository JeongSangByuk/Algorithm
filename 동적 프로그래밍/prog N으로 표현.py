import sys
from collections import deque

# https://ljw538.tistory.com/72

input = sys.stdin.readline

def solution(N, number):

    # N을 이어 붙인 수를 우선 넣어 놓는다.
    arr = [None] + [{int(str(N) * i)} for i in range(1,9)]

    # 최대 8개까지의 n을 사용할 수 있기 때문에
    for i in range(1,9):

        # i개의 n을 사용해서 만들 수 있는 수는 i-1 개의 n까지를 사용해서 만들 수 있는 수의 조합
        for j in range(1,i):

            for num1 in arr[j] :
                for num2 in arr[i-j]:
                    arr[i].add(num1 + num2)
                    arr[i].add(num1 - num2)
                    arr[i].add(num1 * num2)

                    if num2:
                        arr[i].add(num1 // num2)

        if number in arr[i] :
            return i

    # 다돌아도 없으면 -1 리턴
    return -1

N = int(input())
number = int(input())

print(solution(N, number))
