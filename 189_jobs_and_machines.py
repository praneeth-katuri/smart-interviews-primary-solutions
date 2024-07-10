for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    dpA = [0] * n
    dpB = [0] * n

    dpA[0] = a[0]
    dpB[0] = b[0]

    for i in range(1, n):
        dpA[i] = min(dpA[i-1], dpB[i-1] + k) + a[i]
        dpB[i] = min(dpB[i-1], dpA[i-1] + k) + b[i]
    print((min(dpA[n-1], dpB[n-1])))