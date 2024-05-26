for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    count = 0
    for i in range(n-1, 0, -1):
        l = 0
        r = i - 1
        while l < r:
            if arr[l] + arr[r] > arr[i]:
                count += r - l
                r -= 1
            else:
                l += 1
    print(count)