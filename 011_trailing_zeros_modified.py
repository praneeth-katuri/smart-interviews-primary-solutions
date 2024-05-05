def ct_z(n):
    c = 0
    while n > 0:
        n //= 5
        c += n
    return c

def f_lb(n):
    l, h = 1, 5 * (n + 1)
    while l < h:
        m = (l+h) // 2
        if ct_z(m) >= n:
            h = m
        else:
            l = m + 1
    return l

def f_ub(n):
    l, h = 1, 5 * (n+1)
    while l < h:
        m = (l + h) // 2
        if ct_z(m) <= n:
            l = m + 1
        else:
            h = m
    return l - 1

def cnt(n):
    l = f_lb(n)
    h = f_ub(n)
    if ct_z(l) == n and ct_z(h) == n:
        return h - l + 1
    else:
        return 0

for _ in range(int(input())):
    print(cnt(int(input())))