t = int(input())
for _ in range(t):
    n = int(input())
    result = 0
    x = 0

    while n != 0:
        prev = n & 1
        n = n >> 1

        next_bit = n & 1
        n = n >> 1

        if next_bit != 0:
            result += 1 << x
        if prev != 0:
            result += (1<<(x+1))
        x += 2
    print(result)