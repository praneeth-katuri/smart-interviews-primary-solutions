mod = 1000000007
from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    freq = defaultdict(int)
    for num in a:
        freq[num] += 1

    uniq = sorted(freq.keys())
    cnt = defaultdict(int)

    for i in range(len(uniq)):
        a = uniq[i]
        a_freq = freq[a]
        for j in range(i, len(uniq)):
            b = uniq[j]
            b_freq = freq[b]
            x = a ^ b
            if a == b:
                current = (a_freq * (a_freq - 1)) // 2
            else:
                current = a_freq * b_freq
            if current > 0:
                cnt[x] += current

    if cnt.get(0, 0) > 0:
        print(0)
        continue

    product = 1
    for x in cnt:
        product = (product * pow(x, cnt[x], mod)) % mod

    print(product)
