t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    freq = {}
    for i in range(k):
        freq[arr[i]] = freq.get(arr[i], 0) + 1

    print(len(freq), end=" ")

    for i in range(k, n):
        freq[arr[i-k]] -= 1
        if freq[arr[i-k]] == 0:
            del freq[arr[i-k]]
        
        freq[arr[i]] = freq.get(arr[i], 0) + 1
        print(len(freq), end = ' ')
    print()