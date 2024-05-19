def interleavings(a, b, idx1, idx2, res, i):
    if idx1 == 0 and idx2 == 0:
        result.append(''.join(res))
    
    if idx1 != 0:
        res[i] = a[0]
        interleavings(a[1:], b, idx1 - 1, idx2, res, i+1)
    
    if idx2 != 0:
        res[i] = b[0]
        interleavings(a, b[1:], idx1, idx2 - 1, res, i+1)

t = int(input())
for _ in range(1, t+1):
    st1, st2 = input().split()
    result = []
    interleavings(st1, st2, len(st1), len(st2), [''] * (len(st1) + len(st2)), 0)
    print(f"Case #{_}:")
    for interleaving in sorted(result):
        print(interleaving)