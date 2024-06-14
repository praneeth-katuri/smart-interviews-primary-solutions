def check_bit(n, k):
    return (n & ( 1 << k))

def gen_subseq(arr):
    res = []
    for i in range( 1 << len(arr)):
        s = 0
        for j in range(len(arr)):
            if check_bit(i, j):
                s += arr[j]
        res.append(s)
    return res

def lower_bound(arr, lb):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if lb <= arr[mid]:
            high = mid
        else:
            low = mid + 1
    return low

def upper_bound(arr, ub):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if ub >= arr[mid]:
            low = mid + 1
        else:
            high = mid
    return low

for _ in range(int(input())):
    n, a, b = map(int, input().split())
    arr = list(map(int, input().split()))
    subs1 = gen_subseq(arr[:(n//2) + 1])
    subs2 = sorted(gen_subseq(arr[(n//2) + 1:]))
    count = 0
    for s in subs1:
        lb = lower_bound(subs2, a-s)
        ub = upper_bound(subs2, b-s)
        count += (ub - lb)
    print(count)