

n, k = map(int, input().split())
g = list(int(input()) for _ in range(n))

g = list(set(g))
g.sort()

# 1 2 3 4 5 6 7 8 9        12
# 1 2 3 4 1 2

# 10
# min(10 - 1, 10 -5, 10 - 12)

dp = [-1] * (k + 1)

for i in g:

    if i > k:
        continue

    dp[i] = 1

for i in range(1, k + 1):

    if dp[i] == 1:
        continue

    t = []

    for j in g:

        if i - j <= 0 or j > k or dp[i - j] == -1:
            continue

        t.append(dp[i - j])

    if len(t) == 0:
        continue

    dp[i] = min(t) + 1

# print(dp)
print(dp[k])












