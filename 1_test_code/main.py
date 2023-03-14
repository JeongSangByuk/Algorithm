import sys

input = sys.stdin.readline

n = int(input())
liquids = list(map(int, input().split()))

ans = float("INF")
ans_left = 0
ans_right = 0

def check(mid, current):

    # 발견하고자 하는 곳은 어딘가? -> 음수에서 양수로 넘어가는 부분 -> 그게 제일 0과 가까운 값
    # ans보다 작은 값

    # ans = 3
    # -2    -1   4  98 100 130
    # 101 100 95 1 1 30
    # f    f   f   t

    tmp = abs(current + liquids[mid])

    return tmp > ans

for i in range(n - 1):

    current = liquids[i]

    lo = i + 1
    hi = n

    while lo + 1 < hi:

        mid = (lo + hi) // 2

        if check(mid, current):
            hi = mid
        else:
            lo = mid

    # print(i, lo, hi)

    # if abs(current + liquids[lo]) < abs(current + liquids[hi]):
    #     t = abs(current + liquids[lo])
    #     tt = lo
    # else:
    #     t = abs(current + liquids[hi])
    #     tt = hi

    t = abs(current + liquids[lo])

    if t < ans:
        ans = t
        ans_left = i
        ans_right = lo

        if t == 0:
            break

print(liquids[ans_left], liquids[ans_right])