def tower_of_hanoi(n, source, target, middle, moves):
    if n == 1:
        moves.append(f"Move 1 from {source} to {middle}")
        moves.append(f"Move 1 from {middle} to {target}")
        return 2
    else:
        count = 0
        count += tower_of_hanoi(n-1, source, target, middle, moves)

        moves.append(f"Move {n} from {source} to {middle}")
        count += 1
        count += tower_of_hanoi(n-1, target, source, middle, moves)
        moves.append(f"Move {n} from {middle} to {target}")
        count += 1

        count += tower_of_hanoi(n-1, source, target, middle, moves)
        return count

for _ in range(int(input())):
    n = int(input())
    moves = []
    t_moves = tower_of_hanoi(n, 'A', 'C', 'B', moves)
    print(t_moves)
    for move in moves:
        print(move)