def solution(k, s):
    vowels = set('aeiou')
    max_len = 0
    left = 0
    count = 0

    for right in range(len(s)):
        if s[right] in vowels:
            count += 1
        
        while count > k:
            if s[left] in vowels:
                count -= 1
            left += 1
        max_len = max(max_len, right-left+1)
    return max_len

for _ in range(int(input())):
    k = int(input())
    s = input()
    print(solution(k, s))