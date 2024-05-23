def solution(arr):
    l = len(str(max(arr))) + 1
    ans = ''
    a = []
    for i in arr:
        a.append(((str(i) * l)[:l], i))
    a.sort(reverse=True)
    for i in a:
        ans += str(i[1])
    return ans

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solution(arr))