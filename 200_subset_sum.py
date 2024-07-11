def subset_sum(arr, k):
    if k > sum(arr):
        return False
    
    dp = [False] * (k + 1)
    dp[0] = True

    for num in arr:
        for j in range(k, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    return dp[k]

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    if subset_sum(arr, s):
        print("YES")
    else:
        print("NO")