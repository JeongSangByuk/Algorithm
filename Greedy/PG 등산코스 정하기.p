import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def solution_fault(n, paths, gates, summits):
    dic = dict()
    answer = [50001, 10000001]

    for i in range(n):
        dic[i + 1] = []

    for i in paths:
        dic[i[0]].append([i[1], i[2]])
        dic[i[1]].append([i[0], i[2]])

    # print(dic)

    que = deque()

    for i in gates:
        visited = set()
        visited.add(i)
        que.append([i, 0, visited, i, False, -1])

    while que:

        node, cnt, visited, start, isCheckedSummit, summitNum = que.popleft()

        for i in dic[node]:

            if i[0] not in visited:

                # 처음으로 봉우리 완료.
                if (not isCheckedSummit) and i[0] in summits:

                    if max(cnt, i[1]) < answer[1]:
                        answer = [i[0], max(cnt, i[1])]
                        continue

                    if max(cnt, i[1]) == answer[1]:

                        # 산봉우리 작을 경우만 교체
                        if i[0] <= answer[0]:
                            answer = [i[0], max(cnt, i[1])]

                    continue

                # 정상적으로 도착한 경우
                # if isCheckedSummit and i[0] == start:
                #
                #     #print(summitNum,cnt)
                #     # intensity 작고
                #
                #     if cnt < answer[1] :
                #         answer = [summitNum,cnt]
                #         continue
                #
                #     if cnt <= answer[1]:
                #
                #         # 산봉우리 작을 경우만 교체
                #         if summitNum <= answer[0]:
                #             answer = [summitNum,cnt]
                #
                #     continue

                # 다른 출발지 도착인 경우 skip
                if i[0] != start and i[0] in gates:
                    continue

                tmp_visited = visited.copy()
                tmp_visited.add(i[0])
                que.append([i[0], max(cnt, i[1]), tmp_visited, start, isCheckedSummit, summitNum])

    return answer


# https://hz25.tistory.com/6
def solution(n, paths, gates, summits):

    def get_min_intensity():
        pq = []  # (intensity, 현재 위치)
        visited = [10000001] * (n + 1)

        # 모든 출발지를 우선순위 큐에 삽입
        for gate in gates:
            heapq.heappush(pq, (0, gate))

            # 출발지 0으로 초기화
            visited[gate] = 0

        # 산봉우리에 도착할 때까지 반복
        while pq:
            intensity, node = heapq.heappop(pq)

            # 산봉우리이거나 더 큰 intensity라면 더 이상 이동하지 않음
            if node in summits_set or intensity > visited[node]:
                continue

            # 이번 위치에서 이동할 수 있는 곳으로 이동
            for weight, next_node in graph[node]:

                # next_node 위치에 더 작은 intensity로 도착할 수 있다면 큐에 넣지 않음
                # (출입구는 이미 0으로 세팅되어있기 때문에 방문하지 않음)
                new_intensity = max(intensity, weight)

                if new_intensity < visited[next_node]:
                    visited[next_node] = new_intensity
                    heapq.heappush(pq, (new_intensity, next_node))

        # 구한 intensity 중 가장 작은 값 반환
        min_intensity = [0, 10000001]

        for summit in summits:
            if visited[summit] < min_intensity[1]:
                min_intensity[0] = summit
                min_intensity[1] = visited[summit]

        return min_intensity


    summits.sort()
    summits_set = set(summits)
    # graph: 등산로 정보
    graph = defaultdict(list)

    for i, j, w in paths:
        graph[i].append((w, j))
        graph[j].append((w, i))

    return get_min_intensity()

n = int(input())
paths = eval(input())
gates = eval(input())
summits = eval(input())

print(solution(n, paths, gates, summits))
