mod = 1000000007
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    decimal_value = 0
    decimal_value =  (1<<x) - 1
    decimal_value = (decimal_value << y) % mod
    print(decimal_value)