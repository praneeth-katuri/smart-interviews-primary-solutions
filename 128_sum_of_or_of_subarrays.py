for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(32):
        c = 0
        for j in range(n):
            if (arr[j] >> i) & 1:
                ans += (c+1)*(n-j)*(1<<i)
                c = 0
            else:
                c += 1
    print(ans)