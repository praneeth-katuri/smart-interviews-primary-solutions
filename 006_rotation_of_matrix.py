def rotate_90_clockwise(n, matrix):
    transpose = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            transpose[j][i] = matrix[i][j]
    
    for row in transpose:
        row.reverse()
    
    return transpose


t = int(input())
for _ in range(t):
    n = int(input())
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    ans_matrix = rotate_90_clockwise(n, matrix)
    print(f"Test Case #{_ + 1}:")
    for row in ans_matrix:
        print(*row)