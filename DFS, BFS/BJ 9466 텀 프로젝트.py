import sys
from collections import deque
import itertools

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
#n = 1

result = []
for i in range(n):
    dic = {}
    visited = set()
    m = int(input())
    g = list(map(int, input().split()))
    answer = 0

    for i in range(1, m + 1):
        dic[i] = g[i - 1]

        if i == g[i-1]:
            answer += 1
            visited.add(g[i-1])

    def dfs(k, cnt, tmp_visited):

        a = 0

        visited.add(k)
        tmp_visited[k] = cnt

        # 이 싸이클에서 이미 방문한적 있다면
        if dic[k] in tmp_visited:
            a = cnt + 1 - tmp_visited[dic[k]]

        if dic[k] not in visited:
            a = dfs(dic[k],cnt+1, tmp_visited)

        return a

    for i in range(1, m + 1):

        if i not in visited:

            # 방문한 순번을 저장하기 위해, 시간 복잡도를 위해 dic으로 구현
            tmp_visited = {}
            answer += dfs(i,0,tmp_visited)

    result.append(m - answer)

print(*result, sep = '\n')