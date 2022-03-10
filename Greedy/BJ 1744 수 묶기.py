import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
p_g = []
m_g = []

for i in range(n):
    k = int(input())

    if k > 0:
        p_g.append(k)
    else:
        m_g.append(k)

answer = 0

p_g.sort(reverse= True)
m_g.sort()

p_g = deque(p_g)
m_g = deque(m_g)

while p_g:
    node1 = p_g.popleft()

    # 하나 더 뽑을 수 없다면 걍 더해주면 된다.
    if p_g:
        node2 = p_g.popleft()

        # 둘중하나가 1일 경우, 그냥 더해주는게 더 이득.
        if node1 == 1 or node2 == 1:
            answer += (node1 + node2)
        else:
            answer += (node1 * node2)
    else:
        answer += node1

while m_g:
    node1 = m_g.popleft()

    if m_g:
        node2 = m_g.popleft()
        answer += (node1 * node2)
    else:
        answer += node1


print(answer)




