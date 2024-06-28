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

def height(root):
    if root is None:
        return -1
    left_height = height(root.left)
    right_height = height(root.right)
    return 1+max(left_height, right_height)

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    root = None
    for num in arr:
        root = insert_bst(root, num)
    tree_height = height(root)
    print(tree_height)