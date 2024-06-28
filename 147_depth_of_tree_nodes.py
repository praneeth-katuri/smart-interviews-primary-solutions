class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def insert_node(root, ele, depth):
    if root is None:
        print(depth, end=" ")
        return Node(ele)
    if root.data < ele:
        root.right = insert_node(root.right, ele, depth+1)
    else:
        root.left = insert_node(root.left, ele, depth+1)
    return root

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    root = None
    for value in arr:
        root = insert_node(root, value, 0)
    print()