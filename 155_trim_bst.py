class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    
def trimBST(root, l, r):
    if root is None:
        return None
    if root.data < l:
        return trimBST(root.right, l, r)
    if root.data > r:
        return trimBST(root.left, l, r)
    root.left = trimBST(root.left, l, r)
    root.right = trimBST(root.right, l, r)
    return root

def preOrder(root):
    if root is None:
        return
    print(root.data, end=" ")
    preOrder(root.left)
    preOrder(root.right)

def insertNode(root, ele):
    if root is None:
        return Node(ele)
    if ele < root.data:
        root.left = insertNode(root.left, ele)
    else:
        root.right = insertNode(root.right, ele)
    return root

for _ in range(int(input())):
    n, l, r = map(int, input().split())
    arr = list(map(int, input().split()))
    root = None
    for ele in arr:
        root = insertNode(root, ele)
    trim = trimBST(root, l, r)
    preOrder(trim)
    print()