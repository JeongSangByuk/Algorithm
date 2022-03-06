
import sys
from collections import deque, defaultdict

input = sys.stdin.readline

n = int(input())

room = []
stack = deque()

for i in range(n):
    room.append(tuple(map(int, input().split())))

# 도착 시간 순으로 정렬 후, 시작 시간 순으로 정렬
room.sort(key= lambda x: (x[1],x[0]))

room = deque(room)

stack.append(room.popleft())

while room:

    node = room.popleft()

    # stack top에 있던 끝나는 시간이 다음 회의의 시작 시간보다 일찍 끝나는 경우
    if stack[-1][1] <= node[0]:
        stack.append(node)

#print(stack)
print(len(stack))
