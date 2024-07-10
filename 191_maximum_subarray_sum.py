def kadane(arr):
    max_sum = float('-inf')
    current_sum = 0
    start = 0
    end = 0
    temp_start = 0

    for i in range(len(arr)):
        current_sum += arr[i]
        if max_sum < current_sum:
            max_sum = current_sum
            start = temp_start
            end = i

        if current_sum < 0:
            current_sum = 0
            temp_start = i + 1
    
    return f"{max_sum} {start} {end}"

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(kadane(arr))