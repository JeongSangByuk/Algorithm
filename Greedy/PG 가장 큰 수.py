

def solution(number, k):
    answer = []

    for num in number:

        # k가 0보다 큰 시점에서 answer의 끝 값이 num 보다 작으면 pop
        while answer and k > 0 and answer[-1] < num:
            answer.pop()
            k -= 1

        # 계속해서 push
        answer.append(num)


    answer = ''.join(answer[:len(number) - k])
    return answer

number = eval(input())
k = int(input())


print(solution(number,k))