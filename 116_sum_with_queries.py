t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    sum_arr = sum(arr)
    q = int(input())
    for _ in range(q):
        i, j, x = map(int, input().split())
        sum_arr += (j-i+1) * x
    print(sum_arr)