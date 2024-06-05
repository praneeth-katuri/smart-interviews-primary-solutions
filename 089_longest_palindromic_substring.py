def check(arr, n):
    ans = 0
    for i in range(n):
        c1 = i
        k = 1
        while ((c1 -k) >= 0 and (c1 + k) < n and arr[c1-k] ==arr[c1 + k]):
            k += 1
        ans = max(ans, 2 * k - 1)

        c2 = i + 1
        c1 = i
        if i + 1 < n and arr[c1] == arr[c2]:
            k = 1
        else:
            continue
        while (c1 - k >= 0 and c2 + k < n and arr[c1 - k] == arr[c2 + k]):
            k += 1
        
        ans = max(ans, 2 * k)
    return ans

for _ in range(int(input())):
    n = int(input())
    arr = input()
    print(check(arr, n))