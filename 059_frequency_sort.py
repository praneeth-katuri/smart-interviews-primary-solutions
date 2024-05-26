def frequency(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    sorted_arr = sorted(arr, key=lambda x: (freq[x], x))
    print(*sorted_arr)
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    frequency(arr)