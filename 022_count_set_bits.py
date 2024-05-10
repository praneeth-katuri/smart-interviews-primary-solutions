t = int(input())
for i in range(t):
    n = int(input())
    ans = 0
    while(n != 0):
        n = n & (n-1)
        ans += 1
    print(ans)