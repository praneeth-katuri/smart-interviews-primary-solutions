t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    uniq = set(arr)
    max_len = 0

    for num in uniq:
        if num - 1 not in uniq:
            current_num = num
            current_length = 1

            while current_num + 1 in uniq:
                current_length += 1
                current_num += 1
            
            max_len = max(max_len, current_length)
    print(max_len)