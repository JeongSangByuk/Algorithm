from collections import Counter

def solution(progresses, speeds):
    answer = []
    now = 0

    while True:

        cnt = 0

        # progress 다더하기
        progresses=[progresses[i]+speeds[i] for i in range(len(speeds))]

        if progresses[now] >= 100:
            cnt+=1

            # now 값 갱신
            while True:
                now+=1

                if now >= len(progresses):
                    break

                if progresses[now] >= 100 :
                    cnt+=1
                else:
                    break

        if cnt != 0:
            answer.append(cnt)

        if now >= len(progresses):
            break

    return answer

progresses = eval(input())
speeds = eval(input())

print(solution(progresses, speeds))