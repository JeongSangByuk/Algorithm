import heapq as Heap

def solution(answers):
    result = []
    answer = []
    student = []

    # 패턴 정의
    student.append([1, 2, 3, 4, 5])
    student.append([2, 1, 2, 3, 2, 4, 2, 5])
    student.append([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])

    for _ in range(0,3):
        answer.append(0)

    for i in range(len(answers)):
        for j in range(len(student)):

            # 값 맞으면 +1
            if answers[i] == student[j][i % len(student[j])]:
                answer[j]+=1

    # max 값과 같으면 삽입
    for i in range(0, 3):
        if answer[i] == max(answer):
            result.append(i + 1)

    return result

answers = eval(input())

print(solution(answers))