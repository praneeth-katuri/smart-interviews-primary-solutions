from collections import deque
import sys
input = sys.stdin.read
data = input().split()

idx = 0
t = int(data[idx])
idx += 1
results = []

for _ in range(t):
    n = int(data[idx])
    k = int(data[idx+1])
    idx += 2
    arr = list(map(int, data[idx:idx+n]))
    idx += n
    
    dq = deque()
    sum_max = 0

    for i in range(k):
        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()
        dq.append(i)
    sum_max += arr[dq[0]]
    
    for i in range(k, n):
        while dq and dq[0] <= i-k:
            dq.popleft()
        
        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()
        dq.append(i)
        sum_max += arr[dq[0]]
    results.append(sum_max)

print(*results, sep='\n')