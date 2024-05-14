t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    bit_count = [0] * 32
    for num in arr:
        for i in range(32):
            if (num >> i) & 1:
                bit_count[i] += 1
    
    result = 0
    for i in range(32):
        if bit_count[i] % 3 != 0:
            result |= (1<<i)
    print(result)