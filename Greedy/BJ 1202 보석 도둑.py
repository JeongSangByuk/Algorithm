import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, k = map(int, input().split())

# 가방 크기순 최소 힙.
gem = []
for _ in range(n):
    heapq.heappush(gem, list(map(int, input().split())))

bag = [int(input()) for _ in range(k)]
bag.sort()

answer = 0
tmp_gem = []

for b in bag:

    # 가방 크기 보다 작은 보석을 최대 힙에 넣는다.
    while gem and b >= gem[0][0]:
        heapq.heappush(tmp_gem, -heapq.heappop(gem)[1])

    # 최대힙에서 보석 꺼내쓰기. 즉 가지고 올 수 있는 가장 큰 보석 가지고 오기.(그리디스럽다!)
    if tmp_gem:
        answer -= heapq.heappop(tmp_gem)
    elif not gem:
        break

print(answer)









