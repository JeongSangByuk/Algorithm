import sys
from collections import deque, defaultdict
import itertools

input = sys.stdin.readline

n = int(input().strip())

street = list(map(int, input().split()))

price = list(map(int, input().split()))

nowPriceIdx = 0
answer = 0

for i in range(len(street)):

    if price[nowPriceIdx] > price[i]:
        nowPriceIdx = i

    answer += price[nowPriceIdx] * street[i]

print(answer)

