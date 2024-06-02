t = int(input())
for _ in range(t):
    s = input()
    seen = set()
    for char in s:
        if char in seen:
            print(char)
            break
        seen.add(char)
    else:
        print(".")