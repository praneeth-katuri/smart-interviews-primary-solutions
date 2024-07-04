import heapq

def connect_rods(arr, n):
    heap = [x for x in arr]
    heapq.heapify(heap)
    res = 0
    while len(heap) > 1:
        temp = heapq.heappop(heap) +  (heapq.heappop(heap))
        res += temp
        heapq.heappush(heap, temp)
    return res

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(connect_rods(arr, n))