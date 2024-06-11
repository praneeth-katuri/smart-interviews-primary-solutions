import sys
input = sys.stdin.read
data = input().split()
t = int(data[0])
index = 1
mod1 = 1000000007
mod2 = 1000000007

for _ in range(t):
    a = data[index]
    b = data[index + 1]
    index += 2
    n, m = len(a), len(b)

    if n > m:
        print(0)
    
    base1 = 26
    base2 = 31

    power1 = pow(base1, n-1, mod1)
    power2 = pow(base2, n-1, mod2)

    hash_a1 = hash_a2 = 0
    for char in a:
        hash_a1 =(hash_a1 * base1 + ord(char)) % mod1
        hash_a2 =(hash_a2 * base2 + ord(char)) % mod2
    
    hash_b1 = hash_b2 = 0
    for c in b[:n]:
        hash_b1 = (hash_b1 * base1 + ord(c)) % mod1
        hash_b2 = (hash_b2 * base2 + ord(c)) % mod2
    
    count = 0
    if hash_a1 == hash_b1 and hash_a2 == hash_b2:
        count += 1
    
    for i in range(n, m):
        hash_b1 = (hash_b1 - ord(b[i-n]) * power1) % mod1
        hash_b2 = (hash_b2 - ord(b[i-n]) * power2) % mod2
        hash_b1 = (hash_b1 * base1 + ord(b[i])) % mod1
        hash_b2 = (hash_b2 * base2 + ord(b[i])) % mod2

        if hash_a1 == hash_b1 and hash_b2 == hash_a2:
            count += 1
    print(count)