t = int(input())
for _ in range(t):
    n = int(input())
    le = list(map(int, input().split()))
    ans =0
    for i in range(n):
            ans ^= (le[i] + le[i])
    print(ans)