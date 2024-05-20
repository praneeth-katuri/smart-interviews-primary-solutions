def bubble_sort(arr):
    total_swaps = 0
    for i in range(len(arr)):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                total_swaps += 1
                swapped = True
        if not swapped:
            break
    return total_swaps
    
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    total_swaps = bubble_sort(arr)
    print(total_swaps)