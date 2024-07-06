mod = 1000000007
factorials = [1]
for _ in range(int(input())):
    n = int(input())
    while len(factorials) <= n:
        next_index = len(factorials)
        next_factorial = (factorials[next_index - 1] * next_index) % mod
        factorials.append(next_factorial)
    print(factorials[n])