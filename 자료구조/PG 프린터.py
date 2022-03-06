from collections import Counter

def solution(priorities, location):
    answer = 0

    while True:

        print(priorities)
        print(location)

        # 우선순위 중 가장 큰 값 구하기
        m = max(priorities)
        cur = priorities.pop(0)

        # cur 값보다 우선 순위 높은게 있을 경우
        if cur < m:

            priorities.append(cur)

            # location 값 재조정
            if location < 1:
                location = len(priorities) - 1
            else :
                location -=1

            continue

        # 우선 순위 높은게 없다 => pop
        location -= 1
        answer += 1

        if location == -1:
            return answer

    return answer

priorities = eval(input())
location = eval(input())

print(solution(priorities, location))