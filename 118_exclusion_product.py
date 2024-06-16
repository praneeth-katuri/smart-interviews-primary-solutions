k = 10**9+7
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    if n == 0:
        print("")
        continue

    left = [0] * n
    right = [0] * n
    ans = [0] * n

    left[0] = arr[0]
    for i in range(1, n):
        left[i] = (left[i-1] * arr[i]) % k
    
    right[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right[i] = (right[i+1] * arr[i]) % k
    
    if n > 1:
        ans[0] = right[1]
        ans[n-1] = left[n-2]

    for i in range(1, n-1):
        ans[i] = (left[i-1] * right[i+1]) % k
    
    print(*ans)