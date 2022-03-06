import sys
from collections import deque, defaultdict
import itertools

input = sys.stdin.readline

n = int(input().strip())
arr = []
dict = {}

for i in range(n):
    arr.append(input().strip())

max_len = len(max(arr, key=len))

# 자리수 채우기
for i in range(len(arr)):
    if len(arr[i]) < max_len:
        arr[i] = "0"*(max_len - len(arr[i])) + arr[i]

for i in range(len(arr[0])):

    for str in arr:

        if str[i] == '0':
            continue

        # 사전에 있으면
        if str[i] in dict:
            dict[str[i]] += (10 ** (len(str) - (i + 1)))
        else :
            dict[str[i]] = (10 ** (len(str) - (i + 1)))

# 정렬
dict = sorted(dict.items(),key= lambda item:item[1], reverse=True)

answer = 0
now = 9

for i in dict:
    answer += now * i[1]
    now -= 1

print(answer)
#print(dict)