import heapq as Heap

def solution(jobs):
    answer = 0
    ready = []
    time = 0
    l = len(jobs)
    while len(jobs) != 0 or len(ready) != 0:

        # 레디큐가 빈경우, jobs 배열 검사
        if len(ready) == 0:

            # 요청 시간 + 실행 시간 짧은순 으로 정렬한다.
            jobs = sorted(jobs, key=lambda x: (x[0], x[1]))
            # print(jobs)

            # time 변수 갱신
            time=jobs[0][0] + jobs[0][1]
            answer+= (time-jobs[0][0])
            jobs.pop(0)

            # 실행하는 도중 요청이 온 경우, jobs 배열에서 삭제하고 레디큐에 삽입.
            tmpL = len(jobs)
            idx = 0
            while idx != tmpL:
                if time >= jobs[idx][0]:
                    ready.append(jobs[idx])
                    jobs.pop(0)
                    tmpL -= 1
                    idx -= 1
                idx+=1

        # 레디큐에 있는 경우.
        else:
            # print(ready)

            # time 변수 갱신
            time += ready[0][1]
            answer += (time - ready[0][0])
            ready.pop(0)

            # 실행하는 도중 요청이 온 경우, jobs 배열에서 삭제하고 레디큐에 삽입.
            tmpL = len(jobs)
            idx = 0
            while idx != tmpL:
                if time >= jobs[idx][0]:
                    ready.append(jobs[idx])
                    jobs.pop(0)
                    tmpL -= 1
                    idx -= 1
                idx+=1

        # 레디큐 실행 시간 순으로 정렬
        if len(ready) != 0:
            ready = sorted(ready, key=lambda x: x[1])

        # print(answer)

    return int(answer/l)

jobs = eval(input())

print(solution(jobs))