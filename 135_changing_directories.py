def process_commands(commands):
    stack = ['/']
    for cmd in commands:
        if cmd.startswith('cd'):
            path = cmd.split(' ', 1)[1].rstrip('/')

            if path.startswith('/'):
                stack = ['/']
                path = path[1:]
            
            if path == "":
                stack = ['/']
                continue
            
            parts = path.split('/')
            for part in parts:
                if part == '..':
                    if len(stack) > 1:
                        stack.pop()
                elif part:
                    stack.append(part + '/')
        elif cmd == 'pwd':
            pwd = ''.join(stack)
            if not pwd.endswith('/'):
                pwd += '/'
            print(pwd)

t = int(input())
for _ in range(t):
    n = int(input())
    commands = [input() for _ in range(n)]
    process_commands(commands)
    if _ < t - 1:
        print()