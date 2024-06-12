def seive(n):
    s = [True] * (n + 1)
    s[0] = s[1] = False
    for p in range(2, int(n**0.5) + 1):
        if s[p]:
            for i in range(p*p, n+1, p):
                s[i] = False
    p = []
    for x in range(len(s)):
        if s[x]:
            p.append(x)
    return s, p

def count_non_rep(n, s, p):
    pre = [False] * (n + 1)
    for i in range(len(p)):
        for j in range(i, len(p)):
            if p[i] + p[j] > n:
                break
            pre[p[i]+p[j]] = True
    
    c = [0] * (n+1)
    for i in range(1, max_n+1):
        c[i] = c[i-1] + (0 if pre[i] else 1)
    return c

max_n = 10**5
s, p = seive(max_n)
count = count_non_rep(max_n, s, p)

for _ in range(int(input())):
    n = int(input())
    print(count[n])