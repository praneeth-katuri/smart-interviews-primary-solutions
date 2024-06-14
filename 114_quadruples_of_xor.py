def quadXOR(a, b, c, d, n):
    ab = []
    cd = []
    mp = {}
    count = 0
    for i in range(n):
        for j in range(n):
            ab.append(a[i] ^ b[j])

    for i in range(n):
        for j in range(n):
            xor_cd = c[i] ^ d[j]
            if xor_cd in mp:
                mp[xor_cd] += 1
            else:
                mp[xor_cd] = 1
    
    for i in ab:
        if i in mp:
            count += mp[i]
    return count

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = list(map(int, input().split()))
    print(quadXOR(a, b, c, d, n))