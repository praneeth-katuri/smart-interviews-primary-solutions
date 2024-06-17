t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    p1, p2 = 0, n-1
    total = 0
    lmax, rmax = a[0], a[n-1]
    while p1 < p2:
        if a[p1] < a[p2]:
            p1 += 1
            lmax = max(lmax, a[p1])
            total += lmax - a[p1]
        else:
            p2 -= 1
            rmax = max(rmax, a[p2])
            total += rmax - a[p2]
    print(total)