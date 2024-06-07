def generate_permutations(s, left, right, result):
    if left == right:
        result.append(''.join(s))
    else:
        for i in range(left, right + 1):
            s[left], s[i] = s[i], s[left]
            generate_permutations(s, left+1, right, result)
            s[left], s[i] = s[i], s[left]

def get_permutations(s):
    s = list(s)
    s.sort()
    result = []
    generate_permutations(s, 0, len(s)-1, result)
    result.sort()
    return result

for _ in range(1, int(input())+1):
    s = input()
    permutations = get_permutations(s)
    print(f"Test Case #{_}:")
    for p in permutations:
        print(p)