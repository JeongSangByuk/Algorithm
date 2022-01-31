
from collections import deque


# 65 / 90
#
a = "ABCDE"

deq = deque()

for i in a:
    deq.append(i)

print(deq.pop())
print(deq.popleft())