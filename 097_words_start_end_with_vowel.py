n = int(input())
n_arr = input().split()
pre = [0] * (n+1)

for i in range(n):
    word = n_arr[i].lower()
    if word[0] in "aeiou" and word[-1] in "aeiou":
        pre[i+1] = pre[i] + 1
    else:
        pre[i+1] = pre[i]

q = int(input())
for _ in range(q):
    i, j = map(int, input().split())
    print(pre[j+1] - pre[i])