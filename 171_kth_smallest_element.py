import heapq

def k_smallest(arr, k):
    max_heap = []
    for num in arr:
        heapq.heappush(max_heap, -num)

        if len(max_heap) > k:
            heapq.heappop(max_heap)
    return -max_heap[0]

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(k_smallest(arr, k))