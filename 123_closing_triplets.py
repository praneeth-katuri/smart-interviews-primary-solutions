for _ in range(int(input())):
    n1 = int(input())
    A = sorted(map(int, input().split()))
    n2 = int(input())
    B = sorted(map(int, input().split()))
    n3 = int(input())
    C = sorted(map(int, input().split()))

    p1 = p2 = p3 = 0
    ans = float('inf')

    while p1 < n1 and p2 < n2 and p3 < n3:
        max1 = max(A[p1], B[p2], C[p3])
        min1 = min(A[p1], B[p2], C[p3])
        ans = min(ans, max1 - min1)
        if min1 == A[p1]:
            p1 += 1
        elif min1 == B[p2]:
            p2 += 1
        else:
            p3 += 1
    print(ans)