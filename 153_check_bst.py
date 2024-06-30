def check_bst(tree, n):
    def in_order_traversal(idx, result):
        if idx >= n or tree[idx] == -1:
            return []
        left_idx = 2 * idx + 1
        in_order_traversal(left_idx, result)
        result.append(tree[idx])
        right_idx = 2 * idx + 2
        in_order_traversal(right_idx, result)
    
    result = []
    in_order_traversal(0, result)
    for i in range(1, len(result)):
        if result[i] <= result[i-1]:
            return False
    return True

for _ in range(int(input())):
    n = int(input())
    tree = list(map(int, input().split())) 
    print('True' if check_bst(tree, n) else 'False')