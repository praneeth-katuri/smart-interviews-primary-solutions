def check(x, y):
    if (x+y) % 3 != 0:
        return "NO"
    
    if 2 *x < y or 2 * y < x:
        return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print(check(x,y))