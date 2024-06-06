def is_subset(a_map, b_map):
    for c in a_map:
        if a_map[c] > b_map.get(c, 0):
            return False
    return True

for _ in range(int(input())):
    a, b = input().split()
    a_map = {}
    for c in a:
        a_map[c] = a_map.get(c, 0) + 1
    
    b_map = {}
    i = j = 0
    ans = float('inf')
    while j < len(b):
        b_map[b[j]] = b_map.get(b[j], 0) + 1
        j += 1

        while is_subset(a_map, b_map):
            ans = min(ans, j-i)
            b_map[b[i]] -= 1
            if b_map[b[i]] == 0:
                del b_map[b[i]]
            i += 1
    print(ans if ans != float('inf') else -1)