for _ in range(int(input())):
    n = int(input())
    r = list(map(int, input().split()))
    g = list(map(int, input().split()))
    b = list(map(int, input().split()))

    dpr = [0] * n
    dpg = [0] * n
    dpb = [0] * n

    dpr[0], dpg[0], dpb[0] = r[0], g[0], b[0]

    for i in range(1, n):
        dpr[i] = min(dpg[i-1], dpb[i-1]) + r[i]
        dpg[i] = min(dpr[i-1], dpb[i-1]) + g[i]
        dpb[i] = min(dpr[i-1], dpg[i-1]) + b[i]
    
    min_cost = min(dpr[n-1], dpg[n-1], dpb[n-1])
    print(min_cost)