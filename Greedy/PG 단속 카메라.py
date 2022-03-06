
def solution(routes):
    answer = 0

    # 진출을 기준으로 정렬
    routes = sorted(routes, key= lambda x:x[1])
    print(routes)

    # 카메라를 최소 값으로
    camera = -30001

    for car in routes:

        # 카메라보다 진입 시간이 늦으면 카메라 하나 세우기
        if camera < car[0]:
            answer += 1
            camera = car[1]

    return answer

def solution2(routes):
    answer = 0

    routes = sorted(routes, key= lambda x:-x[0])
    print(routes)

    camera = 30001

    for car in routes:
        if camera > car[1]:
            answer += 1
            camera = car[0]

    return answer


routes = eval(input())

print(solution2(routes))