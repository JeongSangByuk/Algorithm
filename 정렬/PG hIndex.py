def solution(citations):

    citations.sort(reverse=True)

    h= 0
    for c in citations:
        if c > h:
            h += 1

    return h

citations = eval(input())

print(solution(citations))