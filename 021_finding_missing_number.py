T = int(input())

for _ in range(T):
    n = int(input())
    ar = list(map(int, input().split()))
    sum_ar = sum(ar)
    sum_con = ((n+1) * (n+2))//2
    missing_num = sum_con - sum_ar
    print(missing_num)