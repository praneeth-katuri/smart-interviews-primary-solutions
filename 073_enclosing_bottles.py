for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    freq = {}
    for r in arr:
        freq[r] = freq.get(r, 0) + 1
    print(max(freq.values()))