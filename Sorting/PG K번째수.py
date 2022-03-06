import heapq as Heap

def solution(array, commands):
    answer = []

    for i in range(len(commands)):

        # slicing
        tmp = array[commands[i][0] - 1:commands[i][1]]

        # sorting
        tmp = sorted(tmp)

        # appending
        answer.append(tmp[commands[i][2] - 1])

    return answer

array = eval(input())
commands = eval(input())


print(solution(array, commands))