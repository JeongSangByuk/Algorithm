def solution(participant, completion):

    # 해시를 사용하기 위해 딕셔너리 생성
    dict = {}

    # 참가자 명단을 돌면서 이미 키값이 있는지 없는지 검사
    for c in participant:

        # 있으면 value 값 +1
        if c in dict:
            dict[c] += 1

        # 없으면 value 값 -1
        else :
            dict[c] = 1

    # 완주자 리스트를 돌면서 value 값 -1
    for c in completion:
        if c in dict:
            dict[c] -= 1

    # vlaue값이 1인 key 반환
    for d in dict:
        if dict[d] == 1:
            return d

participant  = input()
completion = input()

print(solution(eval(participant),eval(completion)))