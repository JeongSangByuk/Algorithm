
import sys

# https://cocook.tistory.com/84

input = sys.stdin.readline

def solution(distance, rocks, n):
    answer = 0

    start, end = 0, distance
    rocks.sort()

    while start <= end:

        # 거리의 최솟값을 mid로 잡는다.
        # 거리가 mid 이하면 다없앤다.
        mid = (start + end)//2

        # 제거한 돌 카운트 변수
        del_stone_cnt = 0

        # 기준이 되는 돌
        pre_stone = 0

        for rock in rocks:

            # 돌사이의 거리가 가정한 mid보다 작으면 제거
            if rock - pre_stone < mid:
                del_stone_cnt += 1

            # 기준 업데이트
            else:
                pre_stone = rock

            if del_stone_cnt > n:
                break

        # 제거 되는 바위가 많아~~ => 범위 줄이기
        if del_stone_cnt > n:
            end = mid - 1

        # 반대 경우
        else:
            answer = mid
            start = mid + 1

    return answer

distance = int(input())
rocks = eval(input())
n = int(input())


print(solution(distance, rocks, n))