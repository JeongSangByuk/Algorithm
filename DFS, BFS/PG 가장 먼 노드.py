
import sys
from collections import deque

input = sys.stdin.readline

def solution(n, edge):

    dict = {}
    visited = {}

    # visited 딕
    for i in range(1, n + 1):
        visited[i] = False

    # 딕셔너리 형식에 양방향 노드 추가.
    for e in edge:

        if e[0] not in dict:
            dict[e[0]] = [e[1]]
        else:
            dict[e[0]].append(e[1])

        if e[1] not in dict:
            dict[e[1]] = [e[0]]
        else:
            dict[e[1]].append(e[0])

    que = deque()

    que.append([1,0])
    answer = [0]
    visited[1] = True

    # bfs 돌린다~
    while que:

        # node[0] = number, node[1] = visit cnt
        node = que.popleft()

        for n in dict[node[0]]:

            # list에서 not in이 아니라 indexing을 이용한 풀이.
            if not visited[n]:
                que.append([n,node[1] + 1])
                visited[n] = True
                answer.append(node[1] + 1)
    #print(answer)

    cnt = 0
    m = max(answer)
    for i in answer:
        if i == m:
            cnt+=1

    return cnt

n = int(input())
vertex = eval(input())

print(solution(n, vertex))