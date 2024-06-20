def solution(arr, n):
    total_sum = 0

    for bit in range(31):
        count = 0
        current_sum = 0

        for i in range(n):
            if (arr[i] >> bit) & 1:
                count += 1
                current_sum += count * (1 << bit)
            else:
                count = 0
        
        total_sum += current_sum
    return total_sum

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solution(arr, n))