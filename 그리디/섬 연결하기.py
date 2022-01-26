
# https://m.blog.naver.com/ndb796/221230994142

cycle_table = []

def getParent(x):

    if cycle_table[x] == x:
        return x

    cycle_table[x] = getParent(cycle_table[x])
    return cycle_table[x]

def unionParent(a,b):
    a = getParent(a)
    b = getParent(b)

    # 더 숫자가 작은 부모로 병합
    if a < b:
        cycle_table[b] = a
    else :
        cycle_table[a] = b

def isSameParent(a, b) :
    a = getParent(a)
    b = getParent(b)

    if a == b :
        return True
    return False

def solution(n, costs):
    answer = 0

    global cycle_table
    for i in range(n):
        cycle_table.append(i)

    # cost값으로 오름차순 정렬
    costs = sorted(costs, key=lambda x:x[2])

    for i in range(len(costs)):

        # 동일한 부모를 가르키지 않는 경우에는 선택
        if not isSameParent(costs[i][0],costs[i][1]):
            answer += costs[i][2]
            unionParent(costs[i][0],costs[i][1])

    return answer

n = int(input())
costs = eval(input())

print(solution(n,costs))