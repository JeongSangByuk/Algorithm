from collections import deque

# 모두다 끝났는지 확인하는 함수
def isFinished(tickets) :

    for t in tickets:
        if t[0] != '0' or t[1] != '0':
            return False

    return True

def solution(tickets):

    answer = []
    que = deque()

    for i, t in enumerate(tickets):

        # 우선 인천 시작 다 append
        if t[0] == "ICN":

            # ticket 배열 복사
            tickets_copy = [items[:] for items in tickets]

            # 다음 목적지를 저장하고 이미 방문한 노드를 0으로 초기화
            next = tickets_copy[i][1]
            tickets_copy[i][0] = '0'
            tickets_copy[i][1] = '0'

            # 복사한 배열, 다음 목적지, answer 배열
            que.append([tickets_copy, next, ['ICN',next]])

    while que:

        # node[0] = ticket array,
        # node[1] = next loca
        # node[2] = answer array
        node = que.popleft()

        # 다 돌면서 출발지가 도착 노드를 찾는다.
        for i, t in enumerate(node[0]):

            # next location과 출발지가 같으면,
            if node[1] == t[0]:

                answer_copy = node[2][:]
                tickets_copy = [items[:] for items in node[0]]

                next = t[1]
                answer_copy.append(next)
                tickets_copy[i][0] = '0'
                tickets_copy[i][1] = '0'

                # 다방문 했는지 검사하고, 적절하면 answer에 append
                if isFinished(tickets_copy) and answer_copy not in answer:
                    answer.append(answer_copy)

                # 복사한 배열, 다음 목적지, answer 배열
                que.append([tickets_copy, next, answer_copy])

    resultIdx = 0
    for i, a in enumerate(answer):
        t = ''.join(a)

        if ''.join(answer[resultIdx]) > t:
            resultIdx = i

    return answer[resultIdx]

tickets = eval(input())

print(solution(tickets))




