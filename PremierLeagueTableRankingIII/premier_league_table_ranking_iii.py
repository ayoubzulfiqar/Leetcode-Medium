import sys

def solve():
    N = int(sys.stdin.readline())
    
    teams = []
    for _ in range(N):
        line = sys.stdin.readline().split()
        name = line[0]
        points = int(line[1])
        goals_for = int(line[2])
        goals_against = int(line[3])
        
        teams.append((name, points, goals_for, goals_against))
        
    teams.sort(key=lambda x: (-x[1], -(x[2] - x[3]), -x[2], x[0]))
    
    for team in teams:
        sys.stdout.write(team[0] + '\n')

solve()