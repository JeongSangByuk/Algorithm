import heapq as Heap

def solution(scoville, K):

    answer = 0

    # heap화 시키기
    Heap.heapify(scoville)

    while True:

        # 스코빌 지수 계산한 후,
        temp1 = Heap.heappop(scoville)
        temp2 = Heap.heappop(scoville)
        s = temp1 + (temp2 * 2)

        # 계산된 값 push
        Heap.heappush(scoville,s)
        answer+=1

        # 가장 적은 값의 스코빌 지수가 K이상이면 break
        if scoville[0] >= K:
            break

        # 원소가 하나 남았으면 1 return
        if len(scoville) <= 1:
            return -1

    return answer

scoville = eval(input())
K = eval(input())

print(solution(scoville, K))
