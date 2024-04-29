t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    sum1 = 0
    for num in arr:
        sum1 += num
    print(sum1)