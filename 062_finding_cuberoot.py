t= int(input())
for _ in range(t):
    n = int(input())
    if n < 0:
        print(-round((-n) ** (1/3)))
    else:
        print(round(n ** (1/3)))