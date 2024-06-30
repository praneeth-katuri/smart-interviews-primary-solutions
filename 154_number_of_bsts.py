class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def build_tree(arr, idx):
    if idx >= len(arr) or arr[idx] == -1:
        return None
    root = Node(arr[idx])
    root.left = build_tree(arr, 2 * idx)
    root.right = build_tree(arr, 2 * idx + 1)
    return root

def count_bsts(root):
    count = 0

    def is_bst(node, min_val, max_val):
        nonlocal count
        if not node:
            return True, float('inf'), float('-inf')
        
        left_is_bst, left_min, left_max = is_bst(node.left, min_val, node.value)
        right_is_bst, right_min, right_max = is_bst(node.right, node.value, max_val)

        if left_is_bst and right_is_bst and left_max < node.value < right_min:
            count += 1
            return True, min(left_min, node.value), max(right_max, node.value)
        return False, float('-inf'), float('inf')
    
    is_bst(root, float('-inf'), float('inf'))
    return count

for _ in range(int(input())):
    n = int(input())
    arr = [-1] * (n+1)
    ele = list(map(int, input().split()))
    for i in range(1, n+1):
        arr[i] = ele[i-1]
    
    root = build_tree(arr, 1)
    count = count_bsts(root)
    print(count)