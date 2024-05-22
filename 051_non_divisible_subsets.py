def solution(arr, n, k):
    f = [0 for i in range(k)]
    for i in range(n):
        f[arr[i] % k] += 1
    if k%2 == 0:
        f[k//2] = min(f[k//2], 1)
    res = min(f[0], 1)
    for i in range(1, k//2 + 1):
        res += max(f[i], f[k-i])
    return res

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solution(arr, n, k))