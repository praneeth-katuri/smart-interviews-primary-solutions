t = int(input())
for _ in range(t):
    n = int(input())
    matrix = []

    for i in range(n):
        matrix.append(list(map(int, input().split())))

    for j in range(n-1, -1, -1):
        sum_diag = 0
        i = 0
        k = j
        while i < n and k < n:
            sum_diag += matrix[i][k]
            i += 1
            k += 1
        print(sum_diag, end=" ")
    
    for i in range(1,n):
        sum_diag = 0
        j = 0
        k = i
        while j < n and k < n:
            sum_diag += matrix[k][j]
            j += 1
            k += 1
        print(sum_diag, end= " ")
    print()