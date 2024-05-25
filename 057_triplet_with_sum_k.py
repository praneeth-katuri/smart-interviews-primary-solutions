def check_triplet(arr,n, k):
    arr.sort()
    for i in range(n-2):
        p1 = i+1
        p2 = n-1

        while p1 < p2:
            sum1 = arr[i] + arr[p1] + arr[p2]

            if sum1 == k:
                return True
            elif sum1 < k:
                p1 += 1
            else:
                p2 -= 1
    return False


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if check_triplet(arr,n,k):
        print("true")
    else:
        print("false")