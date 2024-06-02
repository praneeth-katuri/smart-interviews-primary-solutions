t = int(input())

for _ in range(t):
    s = input().strip()
    vowels = ['a','e','i','o','u']
    max_length = 0
    curr_length = 0

    for char in s:
        if char not in vowels:
            curr_length += 1
        else:
            max_length = max(max_length, curr_length)
            curr_length = 0
    max_length = max(max_length, curr_length)

    print(max_length)