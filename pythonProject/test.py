import sys
import heapq
from collections import deque, defaultdict
import itertools

input = sys.stdin.readline

dic = {}

dic[0] = [1,2,3]
dic[1] = [4]
dic[2] = [5]
dic[3] = []
dic[4] = []
dic[5] = []

def dfs(n):
    print(n)

    for i in dic[n]:

        if i == 4:
            return "NO"

        ans = dfs(i)

        if ans == "NO":
            return "NO"

    return "YES"

dfs(0)