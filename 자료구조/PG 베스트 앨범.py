from collections import Counter


def solution(genres, plays):
    answer = []
    dic = {}

    # 재생횟수 장르별로 다 더하기
    for g,p in zip(genres,plays):
        if g not in dic:
            dic[g] = p
        else:
            dic[g]+=p

    # 재생 횟수를 기준으로 sort
    dic = dict(sorted(dic.items(),key=lambda x:x[1], reverse=True))

    for music in dic:
        temp = []

        # 장르안에서 재생 횟수를 기준으로 sort
        for e in zip(genres, plays, range(len(plays))):
            if music == e[0]:
                temp.append([e[2],e[1]])

        # play value 순으로 sort
        temp = sorted(temp, key=lambda x:x[1], reverse=True)

        # len가 1이면 바로 append
        if len(temp) == 1:
            answer.append(temp[0][0])

        else:
            # 재생횟수가 같으면 고유번호가 낮은 순으로 swap
            if temp[0][1] == temp[1][1]:
                if temp[0][0] > temp[1][0]:
                    temp[0],temp[1] = temp[1],temp[0]

            answer.append(temp[0][0])
            answer.append(temp[1][0])

    return answer

genres = eval(input())
plays = eval(input())

print(solution(genres, plays))