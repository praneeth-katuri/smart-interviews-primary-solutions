for _ in range(int(input())):
    a = input()
    b = input()
    q = int(input())
    for z in range(q):
        i, j, k, l = map(int, input().split())
        m = a[i:j+1]
        n = b[k:l+1]
        if m==n:
            print("Yes")
        else:
            print("No")