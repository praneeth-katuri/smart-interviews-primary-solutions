mod = 1000000007
def a_power_b(a, b, mod):
    result = 1
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % mod
        a = (a**2) % mod
        b //= 2
    return result

def find(n):
    low, high = 1, 2 * (10**14)
    while low < high:
        mid = (low + high) // 2
        if mid * (mid - 1) // 2 < n:
            low = mid + 1
        else:
            high = mid
    k = low - 1
    j = n - (k * (k - 1) // 2) - 1
    return (a_power_b(2, k, mod) + a_power_b(2, j, mod)) % mod

for _ in range(int(input())):
    n = int(input())
    result = find(n) % mod
    print(result)