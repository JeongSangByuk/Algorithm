import sys
from collections import deque, defaultdict
import itertools

# 3의 배수 판별법 : 각자리수를 다 더해서 3의 배수면 3의 배수다
# 넘 수학적인 지식을 이용한 문제 아닌가..?

input = sys.stdin.readline

n = list(input().strip())

n.sort(reverse=True)

s = 0

for i in n:
    s += int(i)

if s % 3 != 0 or "0" not in n:
    print("-1")
else:
    print(''.join(n))


