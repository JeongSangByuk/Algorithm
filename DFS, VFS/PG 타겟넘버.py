from collections import deque
import copy

def solution(numbers, target):
    answer = []

    # dfs 활용
    que = deque()
    que.append([numbers,0])
    cnt = 0

    while que:

        node = que.pop()

        # dfs의 맨 마지막 노드에서 검사
        if node[1] == len(numbers):
            if sum(node[0]) == target:
                cnt += 1

        if node[1] < len(node[0]):

            # 딥카피 보다는 slicing을 이용하자.
            # 두개 넣는다.

            #tmp = copy.deepcopy(node[0])
            tmp = node[0][:]
            que.append([tmp,node[1] + 1])

            tmp2 = node[0][:]
            tmp2[node[1]] *= -1
            que.append([tmp2,node[1] + 1])
        #print(que)

    return cnt

numbers = eval(input())
target = int(input())

print(solution(numbers,target))




