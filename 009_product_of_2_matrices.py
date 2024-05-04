t = int(input())
for i in range(t):
    A = []
    B = []
    n1, m1 = map(int, input().split())
    for i in range(n1):
        A.append(list(map(int, input().split())))
    n2, m2 = map(int, input().split())
    for i in range(n2):
        B.append(list(map(int, input().split())))
    C = [ [0 for i in range(m2)] for j in range(n1) ]
    for i in range(n1):
        for j in range(m2):
            for k in range(n2):
                C[i][j] += A[i][k] * B[k][j]
            print(C[i][j], end=" ")
        print()