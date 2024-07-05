class Node:
    def __init__(self):
        self.c = [None, None]

def insert(r, x):
    n = r
    for i in range(31, -1, -1):
        b = (x >> i) & 1
        if not n.c[b]:
            n.c[b] = Node()
        n = n.c[b]

def find(r, x):
    n = r
    res = 0
    for i in range(31, -1, -1):
        b = (x >> i) & 1
        tb = 1 - b
        if n.c[tb]:
            res += (1 << i)
            n = n.c[tb]
        else:
            n = n.c[b]
    return res

def solve(a):
    r = Node()
    m = 0
    for x in a:
        insert(r, x)
    for x in a:
        m = max(m, find(r, x))
    return m

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a))