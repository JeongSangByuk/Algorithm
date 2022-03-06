from collections import Counter


def solution(bridge_length, weight, truck_weights):
    answer = 0

    # 모든 트럭의 현재 진행 정도를 담는 배열
    progress = [0 for _ in range(len(truck_weights))]

    # 첫 번째 트럭 이미 올라간 상태라고 생각,
    now = 0
    end = now + 1
    w = truck_weights[now]
    progress[0] = 1

    while True:

        print(progress)
        print("now : " + str(now))
        print("end : " + str(end))
        print("w : " + str(w))

        # 다리에 다음 차가 올라 갈 수 있으면 올리기
        if end < len(truck_weights) and w + truck_weights[end] <= weight:
            w+=truck_weights[end]
            end+=1

        # 올라가 있는 모든 차에 대하여 +1
        for i in range(now, end):
            progress[i]+=1
        answer += 1

        # 도착한 차가 있으면 무게를 빼주고 now 변수 최신화
        if progress[now] >= bridge_length:
            w-= truck_weights[now]
            now+=1

            # 종료할 경우
            if now >= len(truck_weights):
                return answer + 2

            continue

    return answer

# 다른 풀이 참조
def solution2(bridge_length, weight, truck_weights):
    from collections import deque

    bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0
    answer = 0

    # 계산의 편의를 위해 리버스
    truck_weights.reverse()

    while truck_weights:

        # 나가는 트럭 무게 빼주기.
        total_weight-=bridge.popleft()

        # 들어올 트럭의 무게가 weight를 넘으면 걍 0 삽입
        if total_weight + truck_weights[-1] > weight:
            bridge.append(0)

        # 들어올 수 있으면 넣어주고 total weight update
        else:
            truck = truck_weights.pop()
            bridge.append(truck)
            total_weight+=truck
        answer+=1

    answer += bridge_length
    return answer

bridge_length = eval(input())
weight = eval(input())
truck_weights = eval(input())
print(truck_weights.pop())
# print(solution(bridge_length, weight, truck_weights))