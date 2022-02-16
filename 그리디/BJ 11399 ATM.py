
import sys
from collections import deque, defaultdict

input = sys.stdin.readline

n = int(input())

people = list(map(int, input().split()))

people.sort()

for i in range(1, len(people)):
    people[i] += people[i-1]

print(sum(people))