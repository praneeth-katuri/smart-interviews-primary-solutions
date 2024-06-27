class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_bst(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert_bst(root.left, value)
    else:
        root.right = insert_bst(root.right, value)
    return root

def check_cbt(root):
    if root is None:
        return True
    queue = [root]
    flag = False
    
    while queue:
        node = queue.pop(0)

        if node:
            if flag:
                return False
            queue.append(node.left)
            queue.append(node.right)
        else:
            flag = True
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    root = None
    for num in arr:
        root = insert_bst(root, num)
    
    if check_cbt(root):
        print("Yes")
    else:
        print("No")