def solution(n, q, arr, queries):
    prefix_sum = [0] * (n+1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + arr[i]
    total = prefix_sum[n]

    for query in queries:
        l, r, k = query
        r_sum = prefix_sum[r+1] - prefix_sum[l]
        new_sum = total - r_sum + k * (r - l + 1)
        print(f"YES {new_sum}" if new_sum % 2 == 1 else "NO")

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = []
    for _ in range(q):
        l, r, k = map(int, input().split())
        queries.append((l, r, k))
    solution(n, q, arr, queries)