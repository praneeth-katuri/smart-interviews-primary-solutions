t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    trie = {}

    cur = trie
    for i in range(31, -1, -1):
        b = 0
        if b not in cur:
            cur[b] = {}
        cur = cur[b]
    
    best = 0
    p = 0
    for x in a:
        p ^= x

        cur = trie
        cur_val = 0
        for i in range(31, -1, -1):
            b = (p >> i) & 1
            tb = 1 - b
            if tb in cur:
                cur |= (1<<i)
                cur = cur[tb]
            else:
                cur = cur.get(b, {})
        if cur_val > best:
            best = cur_val
        
        cur = trie
        for i in range(31, -1, -1):
            b = (p >> i) & 1
            if b not in cur:
                cur[b] = {}
            cur = cur[b]
    print(best)