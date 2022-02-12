
import sys

input = sys.stdin.readline

# 실패한 풀이.
def isFinished(n, judge):

    # n == 0이며 judge 배열이 전부 0이면 종료

    if n != 0:
        return False

    for i in judge:
        if i != 0:
            return False

    return True

# 실패한 풀이.
def solution1(n, times):

    times.sort()

    judge = [0] * len(times)

    now = 0

    while True:

        for i in range(len(judge)):

            # 현재 심사 가능일 경우.
            if judge[i] == 0 and n > 0:
                judge[i] = times[i]
                n -= 1

            start = 0
            end = len(judge) - 1

            if n == 0:
                while start < end:

                    if judge[start] != 0:
                        start += 1
                        continue

                    if judge[start] == 0 and times[start] < judge[end]:
                        judge[start] = times[start]
                        judge[end] = 0
                        start += 1

                    end -= 1

            # 시간이 흐르면서 -1
            if judge[i] > 0:
                judge[i] -= 1

        now += 1

        # 다 끝났는지 확인
        if isFinished(n,judge):
            return now

    return now

def solution(n, times):
    answer = 0

    # right는 가장 비효율적인 경우, 즉 가장 오래걸리는 사람한테만 검사 받는 경우
    left = 1
    right = max(times) * n

    while left <= right:

        mid = (left + right) // 2
        people = 0

        for time in times:

            # people = 모든 심사관들이 mid분동안 심사한 사람의 수
            people += mid // time

            # 검사한 사람의 수가 n명을 넘어가면 break
            if people >= n:
                break

        if people >= n:
            right = mid - 1

        elif people < n:
            left = mid + 1

        answer = left

    return answer


n = int(input())
times = eval(input())

print(solution(n,times))