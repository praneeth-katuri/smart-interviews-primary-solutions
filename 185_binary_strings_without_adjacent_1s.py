k = 1000000007
dp = [0] * 100001
dp[0] = 1
prev_0 = 1
prev_1 = 0
for i in range(1, 100001):
    curr_0 = (prev_0 + prev_1) % k
    curr_1 = prev_0
    dp[i] = (curr_0 + curr_1) % k
    prev_0 = curr_0
    prev_1 = curr_1

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])