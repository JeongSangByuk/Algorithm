import copy
import sys
import math
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def solution(fees, records):

    answer = dict()

    time = dict()

    dic = dict()


    for r in records:

        if not r[6:10] in dic:
            dic[r[6:10]] = [r[0:5]]
        else:
            dic[r[6:10]].append(r[0:5])

    for d in dic:
        if len(dic[d]) % 2 != 0:
            dic[d].append('23:59')

    for d in dic:

        l = len(dic[d])

        for i in range(l):

            if i % 2 != 0:
                continue

            h = int(dic[d][i + 1][0:2]) - int(dic[d][i][0:2])

            m = int(dic[d][i + 1][3:5]) - int(dic[d][i][3:5])

            if m < 0:
                m = m + 60
                h -= 1

            total_m = h * 60 + m

            if d not in time:
                time[d] = total_m
            else:
                time[d] += total_m

    #print(time)
    for t in time:

        total_m = time[t]

        if total_m <= fees[0]:
            answer[t] = fees[1]

        else :

            total_m -= (fees[0])

            tmp_m = math.ceil(total_m / fees[2]) * fees[3]
            #print(tmp_m)
            answer[t] = fees[1] + tmp_m

    result = []

    id = answer.keys()
    id = sorted(id)
    for i in id:
        result.append(answer[i])

    return result

fees = eval(input())
records = eval(input())
print(solution(fees,records))





