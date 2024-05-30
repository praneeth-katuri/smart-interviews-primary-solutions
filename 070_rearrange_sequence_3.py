def solution(arr, n):
    ans = 1
    for i in range(n):
        mini = arr[i]
        maxi = arr[i]
        uniq = set()
        for j in range(i, n):
            uniq.add(arr[j])
            maxi = max(maxi, arr[j])
            mini = min(mini, arr[j])
            if maxi - mini == len(uniq) - 1 and (j - i + 1) > ans:
                ans = j - i + 1
    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solution(arr, n))