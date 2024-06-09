n = int(input())
arr= list(map(int, input().split()))

prefix_sum = [0] * n
prefix_sum[0] = arr[0]
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

q = int(input())
for _ in range(q):
    i, j = map(int, input().split())

    if i == 0:
        print(prefix_sum[j])
    else:
        print(prefix_sum[j] - prefix_sum[i-1])