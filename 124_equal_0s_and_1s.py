t = int(input())
for _ in range(t):
    n = int(input())
    st = input()
    a = list(map(int, st.split()))
    s = 0
    max_length = 0
    map1 = {0: -1}
    for i in range(n):
        if a[i] == 0:
            s -= 1
        else:
            s += 1
        
        if s not in map1:
            map1[s] = i
        else:
            max_length = max(max_length, i-map1[s])
    print(max_length)