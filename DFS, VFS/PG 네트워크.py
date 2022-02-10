from collections import deque

def solution(n, computers):

    answer = 0
    visited = []
    que = deque()

    def bfs():

        while que:
            node = que.popleft()

            if node not in visited:
                visited.append(node)

            for i in range(n):

                # 양방향 연결이 때문에 y축에서만 봐도 된다.
                # 연결돼 있고 방문하지 않은 노드만 que에 삽입
                if computers[node][i] == 1 and i not in visited:
                    que.append(i)

    # 모든 좌표를 돌면서 1인 곳부터 BFS 돌린다.
    for y in range(n):

        # 큐 초기화
        que.clear()

        # 어차피 방문한 곳이면 이미 bfs 다 돌았기 때문.
        if y in visited:
            continue

        for x in range(n):

            if y == x:
                continue

            # 1인 경우만 que에 삽입(bfs 방식)
            if computers[y][x] == 1 and x not in visited:
                que.append(x)

                if x not in visited:
                    visited.append(x)
                    visited.append(y)

                answer += 1

        # 위에서 큐에 넣은 것을 bfs 돌린다.
        bfs()

    # 단독적인 경우를 더 해준다.
    return answer + n - len(visited)


n = int(input())
computers = eval(input())

print(solution(n,computers))




