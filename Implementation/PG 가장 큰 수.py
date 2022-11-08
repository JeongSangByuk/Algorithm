def solution(numbers):

    numbers = [str(n) for n in numbers]
    
    # 비교를 위한 str 3 곱하기
    numbers = sorted(numbers,key= lambda x:x*3, reverse=True)

    return str(int(''.join(numbers)))

numbers = eval(input())

print(solution(numbers))