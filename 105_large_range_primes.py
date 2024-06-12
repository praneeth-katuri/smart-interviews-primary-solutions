def sieve(n):
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    primes = []
    for i in range(2, n+1):
        if sieve[i]:
            primes.append(i)
    return primes

def solution(m, n, primes):
    if m < 2:
        m = 2
    size = n-m+1
    is_prime = [True] * size
    for p in primes:
        start  = max(p*p, m + ((p - m % p) % p))
        for j in range(start, n+1, p):
            is_prime[j - m] = False
    prime_nums = []
    for i in range(size):
        if is_prime[i]:
            prime_nums.append(m + i)
    return prime_nums

for _ in range(int(input())):
    m, n = map(int, input().split())
    primes = sieve(int(n**0.5) + 1)
    prime_nums = solution(m, n, primes)
    print(*prime_nums, sep='\n')