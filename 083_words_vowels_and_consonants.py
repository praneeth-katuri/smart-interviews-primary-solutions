def solution(scentence):
    scentence = scentence.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = len(scentence.split())
    vowels_count = sum(1 for char in scentence if char in vowels)
    cons_count = sum(1 for char in scentence if char.isalpha() and char not in vowels)
    print(words, vowels_count, cons_count)

t = int(input())

for _ in range(t):
    scentence = input()
    solution(scentence)