import heapq
import sys

def solution(n, paths, gates, summits):

    def get_min_intensity():
        pq = []  # (intensity, 현재 위치)
        visited = [10000001] * (n + 1)

        # 모든 출발지를 우선순위 큐에 삽입
        for gate in gates:
            heapq.heappush(pq, (gate,0))

            # 출발지 0으로 초기화
            visited[gate] = 0

        while pq:

            node, intensity = heapq.heappop(pq)

            if node in summits or intensity > visited[node]:
                continue

            for next_node,weight in graph[node]:

                ni = max(intensity,weight)

                if ni < visited[next_node]:
                    visited[next_node] = ni
                    heapq.heappush(pq, (new_intensity, next_node))


