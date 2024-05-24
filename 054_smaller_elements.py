def count_smaller_elements(arr, n):
    def merge_and_count(arr, temp, left, right, result):
        if left == right:
            return
        mid = (left + right) // 2
        merge_and_count(arr, temp, left, mid, result)
        merge_and_count(arr, temp, mid+1, right, result)
        merge(arr, temp, left, mid, right, result)

    def merge(arr, temp, left, mid, right, result):
        i = left
        j = mid + 1
        k = left
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                result[i] += (j-mid-1)
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
            k += 1
            
        while i<= mid:
            temp[k] = arr[i]
            result[i] += (j-mid -1)
            i += 1
            k += 1
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1
            
        for i in range(left, right+1):
            arr[i] = temp[i]
    temp = [0] * n
    result = [0] * n
    merge_and_count(arr, temp, 0, n-1, result)
    return result

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = count_smaller_elements(arr, n)
    print(sum(result))