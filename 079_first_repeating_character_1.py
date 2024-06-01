t = int(input())
for _ in range(t):
    s = input()
    seen = {}
    for char in s:
        if char in seen:
            seen[char] += 1
        else:
            seen[char] = 1

    for char in s:
        if seen[char] > 1:
            print(char)
            break
    else:
        print(".")