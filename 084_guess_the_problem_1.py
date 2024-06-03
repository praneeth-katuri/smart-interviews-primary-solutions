def solution(A, B):
    set_B = set(B)

    result = [char for char in B if char not in A]
    string = ''.join(result)
    print(string)

t = int(input())
for _ in range(t):
    A, B = input().split()
    result = solution(A, B)