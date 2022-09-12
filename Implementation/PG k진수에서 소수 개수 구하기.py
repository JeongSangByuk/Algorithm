import copy
import sys
import math
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def make(num,base):

    tmp = ""
    while num:
        tmp = str(num % base) + tmp
        num = num//base
    return tmp

# 소수 판별
def is_prime_number(x):

    if x == 1 or x == 0:
        return False

    for i in range (2, int(math.sqrt(x) + 1)):
    	if x % i == 0:
        	return False
    return True

def solution(n, k):
    answer = 0

    primeN = str(make(n,k))

    l = len(primeN)

    #print(primeN)

    i = 0
    start = 0

    while i < l:

        if primeN[i] != str(0) and i != l -1:
            i += 1
            continue


        if i == l - 1:
            p = primeN[start:l]
        else:
            p = primeN[start:i]

        if is_prime_number(int(p)):
            #print(int(p))
            answer += 1
        start = i
        i += 1

    return answer

print(solution(110011,10))






