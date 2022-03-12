
import heapq
from collections import deque

l = [1,2,3,4]
que = deque(l)

q = deque(list(que)[:])
print(q.popleft())


