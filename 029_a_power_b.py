mod = 1000000007
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    result = 1
    base = A % mod
    exponent = B
    
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        exponent = exponent//2
        base = (base * base) % mod
    
    print(result)