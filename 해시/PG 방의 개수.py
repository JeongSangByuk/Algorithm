
import sys
from collections import deque, defaultdict

# https://bellog.tistory.com/147

input = sys.stdin.readline

def solution(arrows):
    answer = 0

    x, y = 0, 0

    visit = defaultdict(list)
    dx, dy = [0,1,1,1,0,-1,-1,-1],[-1,-1,0,1,1,1,0,-1]

    for a in arrows:
        print(visit)

        # 노드가 없는 지점에서 교차하는 지점이 생긴다!
        for _ in range(2):
            nx = x + dx[a]
            ny = y + dy[a]

            # 방문 했던 점이지만 경로가 겹치지 않을 경우. answer + 1
            if (nx,ny) in visit and (x,y) not in visit[(nx,ny)]:
                answer += 1

                # 그래프 경로의 표시
                visit[(x, y)].append((nx,ny))
                visit[(nx, ny)].append((x, y))

            # 방문하지 않은 경우
            elif (nx,ny) not in visit:

                # 그래프 경로의 표시
                visit[(x, y)].append((nx,ny))
                visit[(nx, ny)].append((x, y))

            x, y = nx, ny

    return answer

arrows = eval(input())

print(solution(arrows))