import collections

def solution(phone_book):

    answer = True

    # 공백 제거
    for p in phone_book:
        p = p.replace(" ","")

    # 사전순 정렬
    phone_book.sort()

    # 반복문을 돌면서 접두인지 검사.
    for i in range(0,len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False

    return answer

# 해시 사용
def solution2(phone_book):

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