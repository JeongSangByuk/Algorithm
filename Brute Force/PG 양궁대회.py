import copy
import sys
import math
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def solution(n, info):

    answer = []
    manswer = 0
    g = [x for x in range(10,-1,-1)]
    #print(info)

    c = list(itertools.combinations_with_replacement(g,n))

    print(c)

    for i in c:

        appeach = 0
        lion = 0

        dic = dict()

        # dict 초기화
        for j in range(0,11):
            dic[j] = 0

        for j in i:
            dic[j] += 1

        for k in range(0,11):

            # 어피치 승
            if info[10 - k] == 0 and dic[k] == 0:
                continue

            elif info[10 - k] >= dic[k]:
                appeach += k
            else:
                lion += k

        if appeach < lion:

            if manswer < lion - appeach:
                manswer = lion - appeach
                answer.clear()
                answer.append(dic)

            elif manswer == lion - appeach:
                answer.append(dic)


    if len(answer) != 0:

        tmp = []
        for a in answer:
            tmp.append([])
            for j in range(11):
                tmp[-1].append(a[10-j])

        k = 10
        print(tmp)
        while True:
            m = 0
            for t in tmp:
                m = max(m,t[k])

            cnt = 0
            idx = -1

            for j,t in enumerate(tmp):

                if t[k] == m:
                    cnt += 1
                    idx = j

            if cnt == 1:
                return tmp[idx]

            k -= 1

        return tmp

    else:
        answer.append(-1)



    return answer

def solution2(n, info):

    answer = [-1]
    manswer = 0
    g = [x for x in range(0,11)]
    #print(info)

    c = list(itertools.combinations_with_replacement(g,n))

    print(c)

    for i in c:

        appeach = 0
        lion = 0

        dic = [0] * 11

        # dict 초기화
        for j in range(0,11):
            dic[j] = 0

        # 점수 넣기
        for j in i:
            dic[10 - j] += 1

        for k in range(0,11):

            # 어피치 승
            if info[k] == 0 and dic[k] == 0:
                continue

            elif info[k] >= dic[k]:
                appeach += 10 - k
            else:
                lion += 10 - k

        if appeach < lion:

            if manswer < lion - appeach:
                manswer = lion - appeach
                answer = dic

    return answer

n = int(input())
info = eval(input())
print(solution2(n,info))



