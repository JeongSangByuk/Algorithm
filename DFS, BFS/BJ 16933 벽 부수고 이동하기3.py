import math
import sys
from collections import deque
from collections import defaultdict
import itertools
import heapq
from bisect import bisect_left

# sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m, k = map(int, input().split())
g = list(list(map(int, input().strip())) for i in range(n))
dy, dx = [1, -1, 0, 0], [0, 0, -1, 1]


def bfs():
    que = deque()
    que.append((0, 0, 0, True, 1))

    visit = list(list([0] * (k + 1) for _ in range(m)) for _ in range(n))

    visit[0][0][0] = 1

    while que:
        # print(que)
        # print(visit)
        y, x, skill_cnt, is_date, cnt = que.popleft()

        if y == n - 1 and x == m - 1:
            return cnt

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if not ((0 <= ny < n) and (0 <= nx < m)) or visit[ny][nx][skill_cnt] != 0:
                continue

            # 낮일 경우 부시고 이동하기
            # 걍 이동할 수 있으면 이동하기
            # 밤일 경우 머무르기

            # 벽이 아닌 경우
            if g[ny][nx] == 0 and visit[ny][nx][skill_cnt] == 0:
                que.append((ny, nx, skill_cnt, not is_date, cnt + 1))
                visit[ny][nx][skill_cnt] = 1

            if skill_cnt < k and visit[ny][nx][skill_cnt + 1] == 0:

                # 낮일 경우 부시고 이동하기
                if is_date and g[ny][nx] == 1 :
                    # 낮에 부시고 이동했으니까 밤이됨.
                    que.append((ny, nx, skill_cnt + 1, False, cnt + 1))
                    visit[ny][nx][skill_cnt + 1] = 1

                if not is_date:
                    # 머무를 경우
                    que.append((y, x, skill_cnt, True, cnt + 1))

    return -1


print(bfs())
