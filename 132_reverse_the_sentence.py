for _ in range(int(input())):
    s = input()
    stack = []
    temp = ""

    for c in s:
        if c == ' ':
            if temp:
                stack.append(temp)
                temp = ""
        else:
            temp += c
    
    if temp:
        stack.append(temp)
    print(" ".join(reversed(stack)))