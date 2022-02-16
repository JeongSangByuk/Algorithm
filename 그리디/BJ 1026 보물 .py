
import sys
from collections import deque, defaultdict

input = sys.stdin.readline

n = int(input())

a, b = [], []

a= list(map(int, input().split()))
b= list(map(int, input().split()))

a.sort(reverse=True)
b.sort()

answer = 0

for i in range(n):
    answer += a[i] * b[i]

print(answer)

