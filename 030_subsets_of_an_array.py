def generate_susbsets(arr, n):
    subsets = []
    def backtrack(start, current_subset):
        if current_subset:
            subsets.append(current_subset[:])
        for i in range(start, n):
            current_subset.append(arr[i])
            backtrack(i+1, current_subset)
            current_subset.pop()
    backtrack(0, [])
    return subsets


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    subsets = generate_susbsets(arr, n)
    for subset in subsets:
        print(*subset)