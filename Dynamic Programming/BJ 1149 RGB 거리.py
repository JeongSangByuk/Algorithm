import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]

for i in range(1,n):

    # 결국 같은 색이 연속해서 못나오기 때문에!! 다른 색의 값의 min값을 취한다.
    rgb[i][0] = rgb[i][0] + min(rgb[i-1][1], rgb[i-1][2])
    rgb[i][1] = rgb[i][1] + min(rgb[i-1][0],rgb[i-1][2])
    rgb[i][2] = rgb[i][2] + min(rgb[i - 1][0], rgb[i - 1][1])

print(min(rgb[n-1]))