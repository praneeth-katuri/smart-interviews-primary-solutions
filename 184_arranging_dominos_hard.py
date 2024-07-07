def solve(dp, max_n):
    mod = 1000000007
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    dp[4] = 5
    for n in range(5, max_n + 1):
        dp[n] = (dp[n-1] + dp[n-2] + (dp[n-5] * 8)) % mod

max_n = 10**6
dp = [0] * (max_n + 1)
solve(dp, max_n)

t = int(input())
for _ in range(t):
    print(dp[int(input())])