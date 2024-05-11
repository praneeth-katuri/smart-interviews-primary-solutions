t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    xor = a ^ b
    count = 0
    while xor:
        count += xor & 1
        xor >>= 1
    print(count)