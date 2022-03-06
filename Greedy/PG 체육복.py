
import copy

def solution(n, lost, reserve):
    answer = [i for i in range(1,n + 1)]

    l = len(lost)
    i = 0

    lost.sort()
    reserve.sort()

    # 자기 자신이 여분이 있는 경우 먼저 삭제
    while i < l:

        t = lost[i]
        if t in reserve:
            lost.remove(t)
            reserve.remove(t)
            i -= 1
            l -= 1

        i += 1

    l = len(lost)
    i = 0

    # 앞 뒤를 따져보고 삭제.
    while i < l:

        isChange = False

        t = lost[i]

        # 앞에 여분이 있는 경우
        if t - 1 in reserve and not isChange:
            lost.remove(t)
            reserve.remove(t - 1)
            isChange = True

        # 뒤에 여분이 있는 경우
        if t + 1 in reserve and not isChange:
            lost.remove(t)
            reserve.remove(t + 1)
            isChange = True

        if isChange :
            i-=1
            l-=1

        i += 1

        #print(lost)

    for i in lost:
        answer.remove(i)

    return len(answer)

n = int(input())
lost = eval(input())
reserve = eval(input())

print(solution(n, lost, reserve))