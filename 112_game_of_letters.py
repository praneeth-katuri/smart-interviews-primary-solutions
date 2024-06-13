for i in range(int(input())):
    s = input()
    count = [0] * 26

    for i in s:
        count[ord(i)-97] += 1
    xor = 0
    for i in range(26):
        xor ^= count[i]
    if xor == 0:
        print("Banta")
    else:
        print("Santa")