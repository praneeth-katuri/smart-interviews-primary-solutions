def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(row, n, board, solutions):
    if row == n:
        solutions.append(["".join("1" if i == col else '0' for col in board) for i in range(n)])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens(row + 1, n, board, solutions)
            board[row] = -1

def print_solutions(n):
    if n == 1:
        print(1)
        return
    if n == 2 or n == 3:
        print(-1)
        return
    board = [-1] * n
    solutions = []
    solve_n_queens(0, n, board, solutions)
    if not solutions:
        print(-1)
        return
    solutions.sort(reverse=True)
    for solution in solutions:
        print('\n'.join(solution))
        print()

for _ in range(int(input())):
    print_solutions(int(input()))