from itertools import permutations

def detectPrime(num):

    # 소수인지 검사
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    num = []
    numList = []

    # 각각의 자리수를 배열에 넣어준다.
    for i in range(len(numbers)):
        num.append(numbers[i])

    # 각각의 순열을 만든후 append
    for i in range(1, len(num) + 1):
        for j in permutations(num, i):
            numList.append(int(''.join(j)))

    # 중복을 없애기 위함
    num = list(set(numList))

    for n in num:

        if int(n) == 0 or int(n) == 1:
            continue

        # 소수면 answer+1
        if detectPrime(int(n)):
            answer+=1

    return answer

numbers = eval(input())

print(solution(numbers))
