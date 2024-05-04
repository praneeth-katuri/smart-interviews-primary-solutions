t = int(input())
for _ in range(t):
    n = int(input())
    mat = []
    for i in range(n):
        row = list(map(int, input().split()))
        mat.append(row)
    
    result = []
    i, j = 0, 0
    r, d, u, l = n-1, n-1, 1, 0
    
    while True:
        count = False
        while j <= r:
            result.append(mat[i][j])
            j += 1
            count = True
        j -= 1
        i += 1
        r -= 1

        while i <= d:
            result.append(mat[i][j])
            i += 1
            count = True
        j -= 1
        i -= 1
        d -= 1

        while j >= l:
            result.append(mat[i][j])
            j -= 1
            count = True
        j += 1
        i -= 1
        l += 1

        while  i >= u:
            result.append(mat[i][j])
            i -= 1
            count = True
        
        j += 1
        i += 1
        u += 1

        if not count:
            break
    print(*result)