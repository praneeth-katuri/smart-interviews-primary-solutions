t = int(input())
for _ in range(t):
    n = int(input())
    arr= list(map(int, input().split()))

    for i in range(n-1, 0, -1):
        index = i
        for j in range(i-1, -1, -1):
            if arr[j] >= arr[index]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]
        print(index, end = " ")
    print()