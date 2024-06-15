for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    b = [0] * n
    maxe = -float('inf')
    
    for _ in range(int(input())):
        i, j, x = map(int, input().split())

        b[i] += x
        if j != n - 1:
            b[j + 1] -= x
    
    a[0] += b[0]
    maxe = a[0]

    for i in range(1,n):
        b[i] += b[i-1]
        a[i] += b[i]
        maxe = max(maxe, a[i])
    
    print(maxe)