t = int(input())
for _ in range(1, t+1):
    n = int(input())
    s = []
    m = []
    print(f"Case {_}:")
    for _ in range(n):
        op = input().split()

        if op[0] == 'A':
            x = int(op[1])
            s.append(x)
            if not m or x >= m[-1]:
                m.append(x)
            else:
                m.append(m[-1])
        elif op[0] == 'R':
            if s:
                s.pop()
                m.pop()
        elif op[0] == 'Q':
            if m:
                print(m[-1])
            else:
                print("Empty")