from collections import deque


n = int(input())
m = int(input())

lines = [list(map(int, input().split())) for _ in range(m)]

g = dict()

visit = []

for l in range(n):
    g[l + 1] = []

for l in lines:
    g[l[1]].append(l[0])
    g[l[0]].append(l[1])

# dfs 재귀
def dfs(start):
    visit.append(start)

    for node in g[start]:
        if node not in visit:
            dfs(node)

# dfs 덱
def dfs2(start):

    deq = deque()

    deq.append(start)
    visit.append(start)

    while deq:
        node = deq.pop()
        if node not in visit:
            visit.append(node)
            deq.append(node)


#print(lines)
#print(g)
dfs(1)

#print(answer)
print(len(visit) - 1)