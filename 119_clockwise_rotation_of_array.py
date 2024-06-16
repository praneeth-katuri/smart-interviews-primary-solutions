def rotate(arr, n, k):
    k = k % n
    arr.reverse()
    arr[:k] = reversed(arr[:k])
    arr[k:] = reversed(arr[k:])

    return arr

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    result = rotate(arr, n, k)
    print(*result)