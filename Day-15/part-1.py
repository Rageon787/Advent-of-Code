grid = []
moves = ""
with open("input.txt") as f:
    ok = True 
    for line in f:
        if line.strip() == "": 
            ok = False 
            continue
        if ok: grid.append(list(line.strip())) 
        else: moves += line.strip()

def simulate(pos, dir): 
    (dx, dy) = dir 
    (i, j) = pos    


    if grid[i][j] == '#': return False
    elif grid[i][j] == '.': return True 
    elif grid[i][j] == '@':
        ok = simulate((i + dx, j + dy), dir)
        if ok: 
            grid[i][j], grid[i + dx][j + dy] = grid[i + dx][j + dy], grid[i][j]
            global robot 
            robot = (i + dx, j + dy)
    elif grid[i][j] == 'O': 
        ok = simulate((i + dx, j + dy), dir)
        if ok: grid[i][j], grid[i + dx][j + dy] = grid[i + dx][j + dy], grid[i][j]
        else: return False  
    return True 
        

n, m = len(grid), len(grid[0])

robot = (0, 0)
for i in range(n):
    for j in range(m):
        if grid[i][j] == '@': 
            robot = (i, j)
for move in moves: 
    if move == '^': simulate(robot, (-1, 0))
    elif move == '<': simulate(robot, (0, -1))
    elif move == '>': simulate(robot, (0, 1))
    else: simulate(robot, (1, 0))
    #  print(move)
    # for g in grid: print(g)
    # print()
ans = 0 
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'O': ans += 100 * i + j
print(ans)
