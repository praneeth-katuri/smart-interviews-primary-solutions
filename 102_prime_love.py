def sieve(n):
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return sieve


def valid_prime(n, sieve):
    s =str(n)
    if '0' in s:
        return False
    for i in range(len(s)):
        prefix = int(s[i:])
        if not sieve[prefix]:
            return False
    return True

cases = []
max_n = 0
for _ in range(int(input())):
    n = int(input())
    cases.append(n)
max_n = max(cases)
primes = sieve(max_n)
valid_primes = []
prefix_sum = [0] * (max_n+1)
count = 0
for n in range(2, max_n+1):
    if primes[n] and valid_prime(n, primes):
        valid_primes.append(n)
        count += 1
    prefix_sum[n] = count
for n in cases:
    print(prefix_sum[n])