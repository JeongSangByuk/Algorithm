import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, k = map(int, input().split())
g = list(map(int, input().split()))

que = deque(g)

#print(dic)

store = []
answer = 0

while que:
    node = que.popleft()

    if node in store:
        continue

    # 멀티탭이 꽉 차지 않았을 경우, 그냥 넣어주기.
    if len(store) < n:
        store.append(node)

    else:

        tmp = deque(list(que)[:])
        tmp_store = store[:]

        # 가장 늦게 나오는거 빼주기.
        while tmp:

            if len(tmp_store) <= 1:
                break

            num = tmp.popleft()
            if num in tmp_store:
                tmp_store.remove(num)

        store.remove(tmp_store[0])
        store.append(node)
        answer += 1

print(answer)


