from collections import Counter

def solution(clothes):

    answer = 1

    # sort
    clothes = dict(clothes)
    clothes = sorted(clothes.items(),key = lambda x:x[1])

    # counter 모듈을 이용해서 각각의 부위수 계산
    counter = Counter(dict(clothes).values())

    for c in counter:
        answer*=(counter[c] + 1)

    return answer-1

str = input()
clothes = eval(str)

print(solution(clothes))