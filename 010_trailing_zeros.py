t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    while n > 0:
        n //= 5
        count += n
    print(count)