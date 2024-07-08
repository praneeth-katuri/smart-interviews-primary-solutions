k = 1000000007
dp = [0] * 100001
dp[0] = 1
for i in range(1, 100001):
    for j in range(1, 7):
        if i - j >= 0:
            dp[i] = (dp[i] + dp[i-j]) % k

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n]%k)