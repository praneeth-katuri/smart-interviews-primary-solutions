def towerOfHanoi(n, source, target, middle):
    if n == 1:
        print(f"Move 1 from {source} to {target}")
        return
    towerOfHanoi(n-1, source, middle, target)
    print(f"Move {n} from {source} to {target}")
    towerOfHanoi(n-1, middle, target, source)

t = int(input())
for _ in range(t):
    n = int(input())
    print(2**n - 1)
    towerOfHanoi(n, 'A', 'C', 'B')