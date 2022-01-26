from collections import deque

def getParent(set, x):
    if set[x] == x:
        return x

    return set[x] = getParent(set,)

def solution(n, costs):
    answer = 0
    return answer


n = int(input())
cost = eval(input())

print(solution(n,cost))