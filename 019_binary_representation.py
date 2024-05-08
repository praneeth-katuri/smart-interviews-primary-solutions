def binary(n):
    if n == 0:
        return 0
    else:
        return (n % 2) + 10 * binary(n//2)

t = int(input())

for _ in range(t):
    n = int(input())
    print(binary(n))