
import sys
from collections import deque

input = sys.stdin.readline


def solution(n, results):
    answer = 0
    out_dic = {}
    in_dic = {}

    for i in range(1,n + 1):
        out_dic[i] = []
        in_dic[i] = []

    for r in results:
        out_dic[r[0]].append(r[1])
        #out_dic[r[0]].append(r[1])

    none_out = [i for i in range(1,n+1)]

    for x in out_dic:
        for k in out_dic[x]:
            if k in none_out:
                none_out.remove(k)

    print(none_out)

    def dfs(ori):
        stack = deque()
        stack.append(ori)

        while stack:


            node = stack.pop()

            for x in out_dic[node]:
                stack.append(x)

                if node not in in_dic[x]:
                    in_dic[x].append(node)

    for i in range(1,n + 1):
        dfs(i)

    print(out_dic)
    print(in_dic)

    for i in range(1, n + 1):
        if len(out_dic[i]) + len(in_dic[i]) == n - 1:
            answer += 1

    return answer

n = int(input())
results = eval(input())

print(solution(n, results))