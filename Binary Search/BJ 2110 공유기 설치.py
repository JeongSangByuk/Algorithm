import sys

input = sys.stdin.readline

n, c = map(int, input().split())
g = list(int(input()) for _ in range(n))

g.sort()

def check(mid):

    # mid는 가장 인접한 공유기 사이 거리.
    # 최소 거리가 mid 이상이 되도록 최대 n개의 공유기를 설치할 수 있는가.

    # 최대 거리가 1이 되도록 하면 최대 9개나 설치해야함
    # 최대 거리가 9이 되도록하면 최대 1개 설치해야함

    # 1 2 4 8 9

    # 1   9
    # T      T T F F
    # 9 4 4 3 3  1

    # 공유기를 최대로 설치하려면 무조건 첫번째에는 넣어야한다.
    cnt = 1
    prev = g[0]

    for i in g:
        if i - prev >= mid:
            cnt += 1
            prev = i

    return cnt >= c

lo, hi = 0, max(g) + 1

while lo + 1 < hi:

    mid = (lo + hi) // 2

    if check(mid):
        lo = mid
    else:
        hi = mid

print(lo)
