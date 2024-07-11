dp = [[0] * 2001 for _ in range(2001)]

def solve(n, r, dp):
    for i in range(n+1):
        for j in range(r + 1):
            if j == 0 or i == j:
                dp[i][j] = 1
            elif j > i:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % 1000000007

solve(2000, 2000, dp)
for _ in range(int(input())):
    n, r = map(int, input().split())
    print(dp[n][r])