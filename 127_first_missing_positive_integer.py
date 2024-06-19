def solution(n, arr):
    x = n + 100

    for i in range(n):
        if arr[i] <= 0 or arr[i] > n:
            arr[i] = x
    
    for j in range(n):
        num = abs(arr[j])
        if num <= n:
            arr[num-1] = -abs(arr[num-1])
    
    for i in range(n):
        if arr[i] > 0:
            return i + 1
    
    return n + 1

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solution(n, arr))