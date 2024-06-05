def check_groups(strings):
    anagram_groups = {}
    for string in strings:
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagram_groups:
            anagram_groups[sorted_string] += 1
        else:
            anagram_groups[sorted_string] = 1

    print(len(anagram_groups))

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    strings = [input().strip() for _ in range(n)]
    check_groups(strings)