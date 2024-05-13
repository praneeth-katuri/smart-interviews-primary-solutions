def can_convert(a, b):
    all_zeros_a = True
    ones_in_b = False

    for c in a:
        if c == '1':
            all_zeros_a = False
            break

    for c in b:
        if c == '1':
            ones_in_b = True
            break

    if all_zeros_a and ones_in_b:
        return False

    a_all_ones = True
    b_has_zeroes = False
    for c in a:
        if c == '0':
            a_all_ones = False
            break

    for c in b:
        if c == '0':
            b_has_zeroes = True
            break

    if a_all_ones and b_has_zeroes:
        return False
    return True

def min_operations(a, b):
    n = len(a)
    diff = 0
    for i in range(n):
        if a[i] != b[i]:
            diff += 1
    if diff == 0:
        return 0
    elif diff == 1:
        return 1
    else:
        return 2

for _ in range(int(input())):
    a = input()
    b = input()

    if not can_convert(a, b):
        print("NO")
    else:
        operations = min_operations(a, b)
        print("YES", operations)