t = int(input())
for _ in range(t):
    k = int(input())
    cost = list(map(int, input().split()))
    
    dp = [float('inf')] * (k+1)
    dp[0] = 0

    for s in range(1, k+1):
        for i in range(1, 7):
            if s >= i:
                dp[s] = min(dp[s], dp[s-i] + cost[i-1])
    print(dp[k])