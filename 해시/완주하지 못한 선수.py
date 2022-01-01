
def solution(participant, completion):
    answer = ''

    for p in participant:
        for c in completion:


    return answer

def pre(input):
    return input.replace('"','').replace('[','').replace(']','').split(',')

participant  = input()
completion = input()

solution(pre(participant),pre(completion))