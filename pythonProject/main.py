import sys
from collections import deque


input = sys.stdin.readline

def solution(N, number):

    answer = 1
    arr = [None] + [{int(str(N) * i)} for i in range(1,9)]

    for i in range(1,9):
        for j in range(1,i):
            for num1 in arr[j] :
                for num2 in arr[i-j]:
                    arr[i].add(num1 + num2)
                    arr[i].add(num1 - num2)
                    arr[i].add(num1 * num2)

                    if num2:
                        arr[i].add(num1 // num2)

        if number in arr[i] :
            print(arr)
            return i

    return answer

N = int(input())
number = int(input())

print(solution(N, number))
