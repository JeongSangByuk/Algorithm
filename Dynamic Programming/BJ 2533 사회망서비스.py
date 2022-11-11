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
g = defaultdict(list)

for i in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited = [False] * (n + 1)

# dp[i][0] = i 노드가 얼리어답터가 아닐 때, 서브 트리에서 얼리어답터의 최소값
# dp[i][1] = i 노드가 얼리어답터일 떼, 얼리어답터의 최소값
dp = [[0,0] for _ in range(n+1)]

def dfs(start):

    visited[start] = 1

    # start가 얼리어답터일 때, 해당 노드의 서브 노드는 얼리어답터가 전부 아니어도된다.
    # 즉, 최소값은 1
    dp[start][1] = 1

    for i in g[start]:
        if not visited[i]:
            dfs(i)

            # 해당 노드가 얼리어답터가 아니면 각각의 자식 노드들은 반드시 얼리어답터여야 한다.
            dp[start][0] += dp[i][1]

            # 해당 노드가 얼리어답터라면, 각각의 자식 노드들은 얼리어탑터여도 되고 아니어도 된다.
            # 때문의 각각 노드의 최소값을 취해서 더한다.
            dp[start][1] += min(dp[i][0], dp[i][1])

dfs(1)
print(dp)
print(min(dp[1][0],dp[1][1]))








