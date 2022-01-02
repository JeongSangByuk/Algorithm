import collections

def solution(phone_book):

    answer = True

    for p in phone_book:
        p = p.replace(" ","")

    phone_book.sort()
    print(phone_book)
    # for p in phone_book:


    return answer

str = input()
phone_book = eval(str)

print(solution(phone_book))