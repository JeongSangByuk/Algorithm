from collections import deque

def solution(people, limit):

    answer = 0

    people.sort()

    start = 0
    end = len(people) - 1

    while start < end:

        # 처음과 끝을 더했을 때 limit 보다 작으면 start와 end 포인트 조정
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1

        # 하나로도 limit을 넘으면
        else:
            end -= 1

        answer += 1

        if start == end:
            answer += 1

    return answer

def solution2(people, limit):
    result = 0
    deque_people= deque(sorted(people))

    while deque_people:
        left = deque_people.popleft()

        if not deque_people:
            return result + 1

        right = deque_people.pop()

        # 다시 넣어주기
        if left + right > limit :
            deque_people.appendleft(left)

        result +=1

    return result

number = eval(input())
k = int(input())


print(solution(number,k))