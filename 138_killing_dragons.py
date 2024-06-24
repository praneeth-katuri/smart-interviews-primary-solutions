for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    t = c = s = 0

    for i in range(n):
        d = b[i] - a[i]
        c += d
        t += d
    
        if c < 0:
            s = i + 1
            c = 0
    
    print(s+1 if t >= 0 else -1)