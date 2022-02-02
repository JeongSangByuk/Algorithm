def solution(brown, yellow):
    answer = []

    w = brown/2 - 1
    h = 1

    while True:

        if (w * 2) + (h * 2) == brown and (w - 2) * h == yellow:
            return [int(w),int((h+2))]

        # 높이를 증가시키면서 값 확인
        if w > h:
            h += 1

        # 세로가 가로보다 커지면 가로 +1 하고 세로 1로 초기화
        else :
            w -= 1
            h = 1

    return answer


brown = eval(input())
yellow = eval(input())

print(solution(brown, yellow))