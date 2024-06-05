def check_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    
    freq1 = {}
    freq2 = {}

    for char in str1:
        if char in freq1:
            freq1[char] += 1
        else:
            freq1[char] = 1

    for char in str2:
        if char in freq2:
            freq2[char] += 1
        else:
            freq2[char] = 1
    
    return freq1 == freq2

t = int(input())
for _ in range(t):
    str1, str2 = input().split()
    if check_anagrams(str1, str2):
        print("True")
    else:
        print("False")