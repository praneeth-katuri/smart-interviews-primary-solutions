def rightTriangle(n):
    for i in range(n+1):
        for j in range(1, n-i+1):
            print(" ", end="")
        for j in range(n-i+1, n+1):
            print("*", end="")
        print()


t = int(input())
for _ in range(t):
    n = int(input())
    print(f"Case #{_+1}:", end="")
    rightTriangle(n)