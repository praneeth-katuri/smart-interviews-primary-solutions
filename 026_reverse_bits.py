def reverse_bits(n):
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n = n >> 1
    return result

t = int(input())
for _ in range(t):
    n = int(input())
    print(reverse_bits(n))