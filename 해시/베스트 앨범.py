from collections import Counter


def solution(genres, plays):
    answer = []
    dic = {}

    list = [[g,p] for g,p in zip(genres,plays)]
    # print(list)

    for g,p in zip(genres,plays):
        if g not in dic:
            dic[g] = p
        else:
            dic[g]+=p

    dic = sorted(dic, reverse=True)

    for music in dic:
        temp = []
        for i,(g, p) in enumerate(zip(genres, plays)):
            if music == g:
                temp.append([i,p])

        # play value 순으로 sort
        temp = sorted(temp, key=lambda x:x[1], reverse=True)

        cnt = 0

        if len(temp) == 1:
            answer.append(temp[0][0])

        else:
            if temp[0][1] == temp[1][1]:
                if temp[0][0] > temp[1][0]:
                    temp[0],temp[1] = temp[1],temp[0]

            answer.append(temp[0][0])
            answer.append(temp[1][0])
        # print(temp)

    return answer

str = input()
genres = eval(str)

str = input()
plays = eval(str)

print(solution(genres, plays))