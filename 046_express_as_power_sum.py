def pow(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        half_pow = pow(x, n//2)  
        return half_pow * half_pow
    else:
        half_pow = pow(x, n//2)
        return x * half_pow * half_pow

def sol(x, n, curr_num, curr_sum):
    ans = 0
    p = pow(curr_num, n)

    while p + curr_sum < x:
        ans += sol(x, n, curr_num + 1, p + curr_sum)
        curr_num += 1
        p = pow(curr_num, n)
    
    if p + curr_sum == x:
        ans += 1
    return ans

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(sol(n, k, 1, 0))