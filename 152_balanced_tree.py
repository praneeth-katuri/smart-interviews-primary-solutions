class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def insert(root, value):
    if not root:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def isBalanced(root):
    def checkHeight(node):
        if not node:
            return 0
        left_height = checkHeight(node.left)
        right_height = checkHeight(node.right)
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1
    return checkHeight(root) != -1

for _ in range(int(input())):
    n = int(input())
    ele = list(map(int, input().split()))
    root = None
    for num in ele:
        root = insert(root, num)
    
    print('Yes' if isBalanced(root) else 'No')