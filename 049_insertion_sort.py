def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        print(j+1, end = " ")
    print("")

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    insertion_sort(arr)