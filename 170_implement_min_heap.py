class MinHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, x):
        self.heap.append(x)
        current = len(self.heap) - 1
        while current > 0:
            parent = (current - 1) // 2
            if self.heap[parent] > self.heap[current]:
                self.heap[parent], self.heap[current] = self.heap[current], self.heap[parent]
                current = parent
            else:
                break
    
    def delMin(self):
        if not self.heap:
            return
        if len(self.heap) == 1:
            self.heap.pop()
            return
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        current = 0
        while True:
            left = 2 * current + 1
            right = 2 * current + 2
            smallest = current
            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest != current:
                self.heap[current], self.heap[smallest] = self.heap[smallest], self.heap[current]
                current = smallest
            else:
                break
    
    def getMin(self):
        if not self.heap:
            return None
        return self.heap[0]

t = int(input())
heap = MinHeap()
for _ in range(t):
    command = input().split()
    if command[0] == 'insert':
        x = int(command[1])
        heap.insert(x)
    elif command[0] == 'delMin':
        heap.delMin()
    elif command[0] == 'getMin':
        res = heap.getMin()
        print('Empty' if not res else f'{res}')