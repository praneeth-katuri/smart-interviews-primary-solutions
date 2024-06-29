from collections import deque

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

def level_order(root):
    if root is None:
        return []
    result = []
    queue = [root]
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.pop(0)
            level.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result

t = int(input())
for _ in range(t):
    n = int(input())
    values = list(map(int, input().split()))
    root = None
    for value in values:
        root = insert_bst(root, value)
    
    levels = level_order(root)
    print("\n".join(" ".join(map(str, level)) for level in levels))

    if _ < t -1:
        print()