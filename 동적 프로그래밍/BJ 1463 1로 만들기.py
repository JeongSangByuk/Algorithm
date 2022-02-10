import sys
from collections import deque

input = sys.stdin.readline().strip

n = int(input())

arr = [0]*(n+1)

for i in range(2, n+1):

    # -1 미리 한 다음에
    arr[i] = arr[i-1] + 1

    # 당연하게도 1보다는 2 혹은 3으로 나눈게 이득.
    if i % 2 == 0:
        arr[i] = min(arr[i], arr[i//2] + 1)
    if i % 3 == 0:
        arr[i] = min(arr[i], arr[i//3] + 1)

print(arr[n])


