class Deque:
    def __init__(self):
        self.items = []
    
    def push_front(self, x):
        self.items.insert(0, x)
    
    def push_back(self, x):
        self.items.append(x)
    
    def pop_front(self):
        if self.is_empty():
            print("Empty")
        else:
            print(self.items.pop(0))
    
    def pop_back(self):
        if self.is_empty():
            print("Empty")
        else:
            print(self.items.pop())
    
    def is_empty(self):
        return len(self.items) == 0

t = int(input())
deque = Deque()

for _ in range(t):
    op = input().split()
    command = op[0]

    if command == "push_front":
        x = int(op[1])
        deque.push_front(x)
    elif command == "push_back":
        x = int(op[1])
        deque.push_back(x)
    elif command == "pop_front":
        deque.pop_front()
    elif command == "pop_back":
        deque.pop_back()