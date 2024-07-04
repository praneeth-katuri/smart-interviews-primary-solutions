import heapq
def solution(arr, n):
    A = []
    B = []
    result = []
    for i in range(n):
        if not A or arr[i] <= -A[0]:
            heapq.heappush(A, -arr[i])
        else:
            heapq.heappush(B, arr[i])

        if len(A) - len(B) > 1:
            heapq.heappush(B, -heapq.heappop(A))
        elif len(B) > len(A):
            heapq.heappush(A, -heapq.heappop(B))
        
        result.append(-A[0])
    print(*result)

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    solution(arr, n)