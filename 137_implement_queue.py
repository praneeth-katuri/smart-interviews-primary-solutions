t = int(input())
queue = []
for _ in range(t):
    operation = input().strip()
    if operation.startswith("Enqueue"):
        op, x = operation.split()
        queue.append(int(x))
    elif operation == "Dequeue":
        if queue:
            print(queue.pop(0))
        else:
            print("Empty")