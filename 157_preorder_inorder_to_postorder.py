class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    root_value = preorder[0]
    root = Node(root_value)

    mid = inorder.index(root_value)

    root.left = build_tree(preorder[1:mid+1], inorder[:mid])
    root.right = build_tree(preorder[mid+1:], inorder[mid+1:])
    return root

def postorder_traversal(root, result):
    if root is None:
        return
    postorder_traversal(root.left, result)
    postorder_traversal(root.right, result)
    result.append(root.value)

results = []
for _ in range(int(input())):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    result = []
    root = build_tree(preorder, inorder)
    postorder_traversal(root, result)
    results.append(result)
for arr in results:
    print(*arr)