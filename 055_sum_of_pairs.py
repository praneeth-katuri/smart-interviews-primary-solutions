def check_sum(arr, k):
    arr.sort()
    p1 = 0
    p2 = n -1
    while p1 < p2:

        current_sum = arr[p1] + arr[p2]

        if current_sum == k:
            return True
        elif current_sum < k:
            p1 += 1
        else:
            p2 -= 1
    return False
t = int(input())
for _ in range(t):
    n, k  = map(int, input().split())
    arr = list(map(int, input().split()))
    print(check_sum(arr, k))