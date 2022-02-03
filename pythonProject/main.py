from collections import deque


def solution(tickets):
    answer = []
    temp = []
    que = deque()

    for i, t in enumerate(tickets):

        # 우선 인천 시작 다 append
        if t[0] == "ICN":
            temp.append([t[0], t[1],i])

    # 사전 순 정렬
    temp.sort(key= lambda x:x[1])

    for i, k in enumerate(temp):

        que.clear()
        answer.append([])
        tickets_copy = [items[:] for items in tickets]

        que.append([k[0], k[1]])
        answer[i].append(k[0])
        answer[i].append(k[1])

        idx = int(k[2])
        tickets_copy[idx][0], tickets_copy[idx][1] = "0", "0"

        while que:
            print(tickets_copy)
            node = que.pop()

            for t in tickets_copy:
                if node[1] == t[0]:
                    que.append([t[0], t[1]])
                    answer[i].append(t[1])
                    t[0], t[1] = "0", "0"
        print("-----------------")

    # for a in answer:
    #     if len(a) == len(tickets)
    return answer

tickets = eval(input())

print(solution(tickets))




