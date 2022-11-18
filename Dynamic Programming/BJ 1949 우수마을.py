import copy
import sys
import math
from collections import deque
from collections import defaultdict
import itertools
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())

v = [0] + list(map(int, input().split()))
g = defaultdict(list)

for i in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

# dp[i][0] = 해당 노드가 우수마을 x 일 때, 최대값
# dp[i][1] = 해당 노드가 우수마을 o 일 때, 최대값
dp = [[0,0] for _ in range(n + 1)]

visited = set()

def dfs(start):

    visited.add(start)

    # 해당 노드가 우수마을일 경우 최대값 1
    dp[start][1] = v[start]

    for i in g[start]:

        if i not in visited:
            dfs(i)

            # 해당 노드가 우수마을이면 자식 노드는 전부 우수마을이 아니어야한다.
            dp[start][1] += dp[i][0]

            # 해당 노드가 우수마을이 아니면, 자식 노드가 우수마을이거나 아니어도 된다.
            dp[start][0] += max(dp[i][0], dp[i][1])

dfs(1)

print(max(dp[1][0], dp[1][1]))










