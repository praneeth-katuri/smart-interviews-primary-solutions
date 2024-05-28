def bs1(arr, x):
    low = 0
    high = len(arr) - 1
    p1 = -1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            p1 = mid
            high = mid - 1
    return p1

def bs2(arr, x):
    low = 0
    high = len(arr) - 1
    p2 = -1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            p2 = mid
            low = mid + 1
    return p2

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
q = int(input())
for _ in range(q):
    x = int(input())
    p1 = bs1(arr, x)
    p2 = bs2(arr, x)
    if p1 == -1:
        print("0")
    else:
        print(p2-p1+1)