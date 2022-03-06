
import sys
from collections import deque, defaultdict

input = sys.stdin.readline

n = int(input())

money = [500,100,50,10,5,1]

n = 1000 - n

answer = 0

i = 0

while n != 0:

    if n // money[i] == 0 :
        i+=1
        continue

    answer += n//money[i]
    n = n - money[i] * (n//money[i])
    i+=1

print(answer)