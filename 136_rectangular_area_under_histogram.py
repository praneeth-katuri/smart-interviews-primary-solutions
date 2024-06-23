for _ in range(int(input())):
    n = int(input())
    h = list(map(int, input().split()))
    s = []
    max_a = 0
    i = 0

    while i < n:
        if not s or h[i] >= h[s[-1]]:
            s.append(i)
            i += 1
        else:
            top = s.pop()
            area = h[top] * (i - s[-1] -1 if s else i)
            max_a = max(max_a, area)
    
    while s:
        top = s.pop()
        area = h[top] * (i -s[-1]-1 if s else i)
        max_a = max(max_a, area)
    print(max_a)