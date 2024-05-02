def gen_pattern(n):
    n *= 2
    for i in range(n):
        row = []
        for j in range(n):
            symbol = '*' if (i//2 + j//2) % 2 == 0 else "-"
            row.append(symbol)
        print(''.join(row))

for _ in range(1, int(input())+1):
    n = int(input())
    print(f"Case #{_}:")
    gen_pattern(n)