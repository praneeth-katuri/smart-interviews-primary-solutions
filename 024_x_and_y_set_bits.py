t = int(input())
M = 1000000007
for _ in range(t):
    x , y = map(int, input().split())
    print(((1 << x) | (1 << y))%M)