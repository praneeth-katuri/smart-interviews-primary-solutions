def floor(arr, x, n):
    left, right = 0, n-1
    floor = -2147483648

    while left <= right:
        mid = (left+right)//2

        if arr[mid] > x:
            right = mid - 1
        elif arr[mid] <= x:
            floor = arr[mid]
            left = mid + 1
    return floor

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

q = int(input())
for _ in range(q):
    x = int(input())
    result = floor(arr, x, n)
    print(result)