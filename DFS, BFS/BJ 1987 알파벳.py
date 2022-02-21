import sys
import heapq
from collections import deque, defaultdict
import itertools

input = sys.stdin.readline

# 상하좌우
dy, dx = [1,-1,0,0], [0,0,-1,1]

h, w = map(int, input().split())

g = [input().strip() for _ in range(h)]
answer = 1

# set, 집합의 개념을 확실히 이해하자!
# 집합은 순서가 없다 -> 때문에 인덱스를 통한 접근이 불가능하다.
# 집합은 중복을 허용하지 않는다.
# 집합에서 pop은 임의의 수를 꺼낸다 -> 어차피 bfs 돌리면 큐 안에 있는 모든 지점에서 돌아가기 때문에 상관이 없어짐.
def bfs():

    global answer

    # deque로 두면 중복 발생으로 인해 시간 초과 발생,
    # set을 사용해보자!!
    # que = deque()
    que = set()

    history = str(g[0][0])

    que.add((0,0,history))

    while que:

        print(que)

        y,x,tmp_history = que.pop()

        for i in range(4):

            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= h:
                continue

            if nx < 0 or nx >= w:
                continue

            if g[ny][nx] not in tmp_history:

                answer = max(answer,len(tmp_history) + 1)
                que.add((ny,nx,tmp_history+g[ny][nx]))

bfs()

print(answer)