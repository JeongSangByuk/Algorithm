import copy
import sys
import math
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

dy, dx = [-1,1,0,0], [0,0,-1,1]

def solution(survey, choices):

    p = [3,2,1,0,1,2,3]
    c = ['R','T','C','F','J','M','A','N']
    dic = dict()

    for i in c:
        dic[i] = 0

    for i, s in enumerate(survey):

        if choices[i] < 4:
            dic[s[0]] += p[choices[i]-1]
        elif choices[i] > 4:
            dic[s[1]] += p[choices[i]-1]

    #print(dic)

    answer = ""

    for i in range(8):

        if i % 2 != 0:
            continue

        if dic[c[i]] < dic[c[i+1]]:
            answer += c[i+1]
        else:
            answer += c[i]
    return answer

survey = eval(input())
choices = eval(input())

print(solution(survey, choices))


