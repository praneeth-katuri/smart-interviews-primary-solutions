def print_hollow_diamond(n):
    if n % 2 == 1:
        n += 1
    mid = n // 2
    for i in range(1, mid+1):
        for j in range(1, mid-i+1):
            print(" ", end="")
        
        if i == 1:
            print("*", end = "")
        else:
            print("*", end = "")
            for j in range(1, 2*i - 2):
                print(" ", end="")
            print("*", end="")
        for j in range(1, mid-i+1):
            print(" ", end="")
        print()
        
    for i in range(mid+1,n):
        for j in range(1, i-mid+1):
            print(" ", end="")
        
        if i == n-1:
            print("*", end = "")
        else:
            print("*", end = "")
            for j in range(1, 2*(n-i) - 2):
                print(" ", end="")
            print("*", end="")
        for j in range(1, i-mid+1):
            print(" ", end="")
        print()

t = int(input())

for _ in range(t):
    print(f"Case #{_+1}:")
    n = int(input())
    print_hollow_diamond(n)