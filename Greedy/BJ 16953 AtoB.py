import sys
from collections import deque
import itertools

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

a, b = map(int, input().split())

# bfs와 greedy 두가지 풀이.

def bfs():
    que = deque()
    que.append((a, 0))

    visited = set()
    visited.add(a)

    while que:

        node, cnt = que.popleft()

        if node > b:
            return -1
        elif node == b:
            return cnt + 1

        for i in (node * 2, int(str(node) + "1")):

            if i not in visited and i <= b:
                que.append((i, cnt + 1))
                visited.add(i)

    return -1

def greedy(a,b):

    cnt = 1
    while True:
        if a == b:
            return cnt
        elif a > b or (b % 10 != 1 and b % 2 != 0):
            return -1
        elif b % 10 == 1:
            b //= 10
            cnt += 1
        elif b % 2 == 0:
            b //= 2
            cnt += 1

#print(bfs())
print(greedy(a,b))





