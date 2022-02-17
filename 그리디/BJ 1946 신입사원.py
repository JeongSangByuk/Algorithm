import sys
from collections import deque, defaultdict
import itertools

input = sys.stdin.readline

n = int(input().strip())

total_people = []
answer = []

def solution(answer):

    m = int(input())
    cnt = 0
    people = []

    for i in range(m):
        people.append(tuple(map(int, input().split())))

    people.sort(key = lambda x: x[0])

    # 결국 솔팅 해놨기 때문에, 0번째 인덱스는 무조건 작고! 1번째 인덱스만 비교하면 되는 것.
    maxValue = people[0][1]

    for i in range(0, m):

        if maxValue > people[i][1]:
            maxValue = people[i][1]
            cnt += 1

    answer.append(cnt + 1)

for i in range(n):
    solution(answer)

for i in range(n):
    print(answer[i])