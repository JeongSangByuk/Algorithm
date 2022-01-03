import collections

def solution(phone_book):

    answer = True

    hash = {}

    for phone_number in phone_book:
        hash[phone_number] = 1

    for phone_number in phone_book:
        temp = ""

        for number in phone_number:
            temp += number

            if temp in hash and temp != phone_number:
                return False

    return answer

str = input()
phone_book = eval(str)

print(solution(phone_book))