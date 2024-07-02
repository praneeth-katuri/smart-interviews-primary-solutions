from collections import deque
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

def left_view(root):
    if root is None:
        return []
    
    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == 0:
                result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    root = None
    for value in arr:
        root = insert(root, value)
    left_view_tree = left_view(root)
    print(*left_view_tree)