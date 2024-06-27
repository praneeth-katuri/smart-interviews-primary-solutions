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

def check_fbt(root):
    if root is None:
        return True
    if (root.left and not root.right) or (root.right and not root.left):
        return False
    return check_fbt(root.left) and check_fbt(root.right)

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    root = None
    for num in arr:
        root = insert_bst(root, num)
    result = check_fbt(root)
    print("True" if result else "False")