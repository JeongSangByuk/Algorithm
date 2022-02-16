
import sys
from collections import deque, defaultdict

input = sys.stdin.readline

s = input().strip()

num = s.replace('-',"+").split("+")
num = list(map(int, num))

i = 0
cnt = 1
answer = num[0]

while i < len(s):

    # 마이너스가 나온 이후로 전부 빼도 된다.
    if s[i] == '-':
        break

    # 초반에 나온 플러스는 그냥 더해주기
    elif s[i] == '+':
        answer += int(num[cnt])
        cnt += 1

    i += 1

l = len(num)

# 마이너스가 나온 시점부터 모든 수 빼줘야 최소
print(answer - sum(num[cnt:l]))

