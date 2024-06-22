for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    res = [1] * n
    st = []

    for i in range(len(arr)-1, -1, -1):
        while st and arr[i] > arr[st[-1]]:
            a = st.pop()
            res[a] = a - i
        st.append(i)
    while st:
        x = st.pop()
        res[x] = x + 1
    print(*res)