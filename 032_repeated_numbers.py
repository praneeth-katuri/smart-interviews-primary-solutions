def merge(arr, left, mid, right):
    p1 = mid - left + 1
    p2 = right - mid
    L = arr[left:mid+1]
    R = arr[mid+1:right+1]

    i = j = 0
    k = left

    while i < p1 and j < p2:
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    while i<p1:
        arr[k] = L[i]
        i += 1
        k += 1
    while i <p2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right)//2
        merge_sort(arr,left, mid)
        merge_sort(arr, mid+1, right)
        merge(arr, left,mid, right)

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    merge_sort(arr, 0, n-1)
    repeated_numbers = []
    for i in range(1,n):
        if arr[i] == arr[i-1] and arr[i] not in repeated_numbers:
            repeated_numbers.append(arr[i])
    print(*repeated_numbers)