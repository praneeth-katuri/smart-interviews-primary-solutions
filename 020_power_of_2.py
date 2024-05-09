T = int(input())
for _ in range(T):
    n = int(input())
    print('False' if n & n-1 else 'True')
