t = int(input())
for _ in range(t):
    s, k = input().split()
    k = int(k)
    result = ""
    for char in s:
        next_char = chr((ord(char) - ord('a') + k ) % 26 + ord('a'))
        result += next_char
    
    print(result)