from math import factorial
for _ in range(int(input())):
    s = input()
    rank = 1
    n = len(s)
    for i in range(n):
        count = 0
        for j in range(i+1, n):
            if s[j] < s[i]:
                count += 1
        rank += count * factorial(n - i - 1)
    print(rank)