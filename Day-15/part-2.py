import sys 
sys.setrecursionlimit(1000000000)
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

def convert(a):
    if a == '.': return '..' 
    elif a == '#': return '##'
    elif a == 'O': return '[]'
    return '@.'
def simulate(pos, dir): 
    (dx, dy) = dir 
    (i, j) = pos    


    if grid[i][j] == '#': return False
    elif grid[i][j] == '@':
        ok = simulate((i + dx, j + dy), dir)
        if ok: 
            grid[i][j], grid[i + dx][j + dy] = grid[i + dx][j + dy], grid[i][j]
            global robot 
            robot = (i + dx, j + dy)

    elif grid[i][j] == ']':
        if dir == (1, 0) or dir == (-1, 0):
            ok = True 
            ok &= simulate((i + dx, j + dy), dir)
            ok &= simulate((i + dx, (j - 1) + dy), dir)
            if ok:
                grid[i][j], grid[i + dx][j + dy] = grid[i + dx][j + dy], grid[i][j]
                grid[i][j - 1], grid[i + dx][(j - 1) + dy] = grid[i + dx][(j - 1) + dy], grid[i][j - 1]
            return ok
        else:
            ok = simulate((i, j - 2), dir) 
            if ok:
                grid[i][j - 1], grid[i][j - 2] = grid[i][j - 2], grid[i][j - 1]
                grid[i][j], grid[i][j - 1] = grid[i][j - 1], grid[i][j] 
            return ok
    elif grid[i][j] == '[': 
        if dir == (1, 0) or dir == (-1, 0):
            ok = True 
            ok &= simulate((i + dx, j + dy), dir)
            ok &= simulate((i + dx, (j + 1) + dy), dir)
            if ok:
                grid[i][j], grid[i + dx][j + dy] = grid[i + dx][j + dy], grid[i][j]
                grid[i][j + 1], grid[i + dx][(j + 1) + dy] = grid[i + dx][(j + 1) + dy], grid[i][j + 1]
            return ok
        else:
            ok = simulate((i, j + 2), dir) 
            if ok:
                grid[i][j + 1], grid[i][j + 2] = grid[i][j + 2], grid[i][j + 1]
                grid[i][j], grid[i][j + 1] = grid[i][j + 1], grid[i][j] 
            return ok
    else: 
        return True 
    return False
        
n, m = len(grid), len(grid[0])

new_grid = []
for i in range(n):
    temp = ""
    for j in range(m):
        temp += convert(grid[i][j])
    new_grid.append(list(temp))

grid = new_grid 
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
    elif move == 'v': simulate(robot, (1, 0))
    else: pass

ans = 0 

for i in range(n):
    for j in range(m):
        if grid[i][j] == '[': ans += 100 * i + j
for g in grid: print(g)
print(ans)
    

