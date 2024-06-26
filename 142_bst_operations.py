class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if not root:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def find_min(node):
    while node.left:
        node = node.left
    return node.value

def delete(root, value):
    if not root:
        return None
    if value < root.value:
        root.left = delete(root.left, value)
    elif value > root.value:
        root.right = delete(root.right, value)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        min_value = find_min(root.right)
        root.value = min_value
        root.right = delete(root.right, min_value)
    return root

def search(root, value):
    if not root:
        return False
    if root.value == value:
        return True
    if value < root.value:
        return search(root.left, value)
    return search(root.right, value)

def preorder(root, result):
    if root:
        result.append(str(root.value))
        preorder(root.left, result)
        preorder(root.right, result)

t = int(input())
for each in range(1, t+1):
    q = int(input())
    queries = []
    for _ in range(q):
        query = input().split()
        a = int(query[0])
        x = int(query[1]) if a != 4 else None
        queries.append((a, x))

    root = None
    output = []
    for query in queries:
        if query[0] == 1:
            root = insert(root, query[1])
        elif query[0] == 2:
            root = delete(root, query[1])
        elif query[0] == 3:
            if search(root, query[1]):
                output.append("Yes")
            else:
                output.append("No")
        elif query[0] == 4:
            result = []
            preorder(root, result)
            output.append(' '.join(result))
    
    print(f"Case #{each}:")
    print(*output, sep='\n')

