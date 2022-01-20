
def isNum(n):

    n = str(n)

    # 1의 자리수는 무조건 한수
    if len(n) == 1:
        return True

    count = int(n[1]) - int(n[0])

    i = 0

    while True:

        # 끝까지 다 돈경우
        if i == len(n) - 1:
            break

        if int(n[i + 1]) - int(n[i]) != count:
            return False
        i+=1

    return True

answer = 0
n = int(input())


for i in range(1,n + 1):
    if isNum(i):
        answer+=1

print(answer)


