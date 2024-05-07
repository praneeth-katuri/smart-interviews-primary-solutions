for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())

    a1 = abs(x2-x1) * abs(y2-y1)
    a2 = abs(x4-x3) * abs(y4-y3)

    xdist = min(x4, x2) - max(x1, x3)
    ydist = min(y4, y2) - max(y1, y3)

    a3 = 0
    if xdist > 0 and ydist > 0:
        a3 = xdist * ydist
    print(a1 + a2 - a3)