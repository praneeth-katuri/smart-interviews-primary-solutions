def check_difference(arr, k):
    seen_elements = set()
    for num in arr:
        if num - k in seen_elements or num+k in seen_elements:
            return True
        seen_elements.add(num)
    return False
t = int(input())
for _ in range(t):
    n, k  = map(int, input().split())
    arr = list(map(int, input().split()))
    if check_difference(arr, k=abs(k)):
        print("true")
    else:
        print("false")