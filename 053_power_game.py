def solution(n, team_a, team_b):
    team_a.sort()
    team_b.sort()

    a = 0
    b = 0
    wins = 0
    while a < n and b < n:
        if team_a[a] > team_b[b]:
            wins += 1
            b += 1
        a += 1
    
    print(wins)

t = int(input())
for _ in range(t):
    n = int(input())
    team_a = list(map(int, input().split()))
    team_b = list(map(int, input().split()))

    result = solution(n, team_a, team_b)