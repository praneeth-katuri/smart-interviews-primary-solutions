t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    l = 0
    r = n - 1
    while l < r:
        while l < r and arr[l] == 0:
            l += 1
        while l < r and arr[r] == 1:
            r -= 1
        
        if l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
    print(*arr)