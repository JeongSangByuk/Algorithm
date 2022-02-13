
import sys
from collections import deque, defaultdict

input = sys.stdin.readline

# 시간 초과 => Dfs, Bfs 할 때, visited 배열 이용하자 꼭!
def solution(n, results):
    answer = 0
    out_dic = {}
    in_dic = {}

    for i in range(1,n + 1):
        # 공집합 선언을 위한 None으로 초기화
        out_dic[i] = {None}
        in_dic[i] = {None}

    for r in results:
        out_dic[r[0]].add(r[1])

    def dfs(ori):
        stack = deque()

        # stack[0] : 현재 노드, stack[1] : 현재 노드의 부모 노드
        stack.append(ori)

        visited = [False] * n

        while stack:

            node = stack.pop()

            visited[node-1] = True

            # pop된 정점에서 out되는 정점 검사
            for x in out_dic[node]:

                if x == None:
                    continue

                # 그 다음 방문하는 정점 append
                if not visited[x-1]:
                  stack.append(x)

                out_dic[ori].add(x)
                in_dic[x].add(ori)


    # 모든 노드에서 dfs 돌린다!
    for i in range(1,n + 1):
        dfs(i)

    #print(out_dic)
    #print(in_dic)

    for i in range(1, n + 1):
        # none 개수 제외
        if len(out_dic[i]) + len(in_dic[i]) == n + 1:
            answer += 1

    return answer

n = int(input())
results = eval(input())

print(solution(n, results))