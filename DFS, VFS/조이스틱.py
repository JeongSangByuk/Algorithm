import copy

# https://programmers.co.kr/questions/11542

# 65 / 90
mid = int((65 + 90) / 2)

def getCount(c) :

    if ord(c) <= mid:
        return ord(c) - 65
    else :
        return 91 - ord(c)

def solution(name):
    moves = [-1, 1]
    nameList = list(name)

    # start = (nameList, index, count)
    def bfs(start):
        stack = [start]

        while stack:
            n = stack.pop()
            array, idx, cnt = n[0], n[1], n[2]

            cnt += getCount(array[idx])
            array[idx] = 'A'

            # 종료 시점 : 전부 A로 치환됐을 때
            if array.count('A') == len(array):
                return cnt
            
            # 양 옆으로 갔을 때 각각의 경우를 stack에 삽입
            for move in moves:
                _array = copy.deepcopy(array)
                _idx = idx + move
                _cnt = cnt + 1
                stack.insert(0,(_array,_idx,_cnt))

    answer = bfs((nameList,0,0))

    return answer

name = eval(input())


print(solution(name))