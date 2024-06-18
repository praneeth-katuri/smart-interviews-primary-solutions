for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n):
        if arr[i] == 0:
            arr[i] = -1
    
    for i in range(1, n):
        arr[i] += arr[i-1]
    
    count = 0
    prefix_sum_count = {}
    prefix_sum_count[0] = 1

    for i in range(n):
        if arr[i] in prefix_sum_count:
            count += prefix_sum_count[arr[i]]
            prefix_sum_count[arr[i]] += 1
        else:
            prefix_sum_count[arr[i]] = 1
    
    print(count)