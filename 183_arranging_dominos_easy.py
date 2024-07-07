def solve(dp, max_n):
    mod = 1000000007
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 1
    dp[5] = 2
    for n in range(6, max_n + 1):
        dp[n] = (dp[n-1] + dp[n-5]) % mod

dp = [0] * 100001
solve(dp, 100000)

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])