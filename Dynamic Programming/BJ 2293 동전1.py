
n, k = map(int, input().split())
g = list(int(input()) for _ in range(n))

dp = [0] * (k + 1)
dp[0] = 1

for i in range(n):

    for j in range(k + 1):

        if j - g[i] < 0:
            continue

        dp[j] += dp[j - g[i]]

print(dp[k])










