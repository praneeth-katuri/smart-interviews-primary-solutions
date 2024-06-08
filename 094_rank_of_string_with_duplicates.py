from math import factorial
for _ in range(int(input())):
    s = input()
    rank = 1
    n = len(s)

    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for i in range(n):
        small_chars = set()
        for j in range(i + 1, n):
            if s[j] < s[i] and s[j] not in small_chars:
                small_chars.add(s[j])
        
        for char in small_chars:
            char_count[char] -= 1

            d = 1
            for k in char_count:
                d *= factorial(char_count[k])
            
            rank += factorial(n - i - 1) // d
            char_count[char] += 1
        char_count[s[i]] -= 1
    print(rank)