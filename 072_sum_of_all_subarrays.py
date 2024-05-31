def sum_arr(arr, n):
    total_sum = 0
    for i in range(n):
        count = (i+1)*(n-i)
        total_sum += arr[i] * count
    return total_sum

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(sum_arr(arr, n))