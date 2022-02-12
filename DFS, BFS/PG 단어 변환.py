from collections import deque

# 바꿀 수 있는지 검사 -> 하나 빼고 다 같으면 바꿀 수 있다.
def canChange(s1,s2):

    cnt = 0

    for t in range(len(s1)):

        if s1[t] != s2[t]:
            cnt += 1

        if cnt > 1:
            return False

    return True


def solution(begin, target, words):
    answer = 0

    que = deque()
    que.append([begin,0,0])

    l = len(words)

    while que:

        #print(que)

        # node[0] = string, node[1] = cnt, node[2] = answer
        node = que.popleft()

        if node[1] >= len(words):
            continue

        for t in range(l):

            # 변화시킬 수 있는 경우 -> 하나빼고 다 같은 경우만이다.
            if not canChange(node[0], words[t]):
                continue

            for i,c in enumerate(words[t]):

                # 다른 부분에 있어서 바꾼다.
                if c != node[0][i]:
                    tmp = list(node[0])
                    tmp[i] = c

                    t = [''.join(tmp),node[1] + 1,node[2] + 1]

                    # target과 똑같으면 return
                    if t[0] == target:
                        return t[2]

                    # 아닐 경우 que에 push
                    if t not in que:
                        que.append(t)

                    # 다른 부분은 하나밖에 없기 때문에 break
                    break

    return answer

begin = eval(input())
target = eval(input())
words = eval(input())

print(solution(begin, target, words))




