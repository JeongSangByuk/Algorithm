import sys
from collections import deque
import itertools
import heapq

sys.setrecursionlimit(10**7)

input = sys.stdin.readline

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]

result = sys.maxsize

def solution_combination() :
    players = [i for i in range(0, n)]
    players_com = list(itertools.combinations(players,int(n/2)))
    visited = set()

    for p in players_com:

        if p in visited:
            continue

        # 반대 팀
        oppo_players = tuple(set([i for i in range(0,n)]) - set(p))

        # visited add
        visited.add(p)
        visited.add(oppo_players)

        power = 0
        power_oppo = 0
        for i in itertools.combinations(p,2):
            power += (g[i[0]][i[1]] + g[i[1]][i[0]])

        for i in itertools.combinations(oppo_players, 2):
            power_oppo += (g[i[0]][i[1]] + g[i[1]][i[0]])

        result = min(result, abs(power-power_oppo))

def solution_backtracking():

    visited = set()
    p = []

    def dfs(now, depth):

        global result

        #print(p , visited, depth)

        if depth == (n//2) and tuple(p) not in visited:

            oppo_p = set([i for i in range(0, n)]) - set(p)

            visited.add(tuple(p))
            visited.add(tuple(oppo_p))

            power = 0
            power_oppo = 0

            for i in itertools.combinations(list(p), 2):
                power += (g[i[0]][i[1]] + g[i[1]][i[0]])

            for i in itertools.combinations(list(oppo_p), 2):
                power_oppo += (g[i[0]][i[1]] + g[i[1]][i[0]])

            result = min(result, abs(power - power_oppo))
            return

        for i in range(now,n):
            p.append(i)
            dfs(i + 1,depth + 1)
            p.remove(i)

    dfs(0, 0)

solution_backtracking()
print(result)



