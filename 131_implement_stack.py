t = int(input())
stack = []
for _ in range(t):
    operation = input().strip()
    if operation.startswith("push"):
        op, x = operation.split()
        stack.append(int(x))
    elif operation == "pop":
        if stack:
            print(stack.pop())
        else:
            print("Empty")