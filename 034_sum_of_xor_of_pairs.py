def sumOfXor(arr, n):
    result = 0
    for bit in range(32):
        count_set = sum((num >> bit) & 1 for num in arr)
        count_unset = n - count_set
        result += (count_set * count_unset) * (1<<bit)   
    return result*2

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(sumOfXor(arr, n))