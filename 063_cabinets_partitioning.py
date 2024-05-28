def partition(arr, n, k):
    low = max(arr)
    high = sum(arr)

    while low < high:
        mid = (low + high) // 2
        if valid(arr, mid, n, k):
            high = mid
        else:
            low = mid + 1
    return low

def valid(ar, mid, n, k):
    count = 1
    total = 0
    for i in range(n):
        if total + arr[i] <= mid:
            total += ar[i]
        else:
            count += 1
            total = arr[i]
    return count <= k

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(partition(arr, n, k))