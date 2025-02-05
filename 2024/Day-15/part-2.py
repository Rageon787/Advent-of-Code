import sys 
sys.setrecursionlimit(1000000000)
grid = []
moves = ""

filename = sys.argv[1]
with open(filename) as f:
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

def check(pos, dir): 
    (dx, dy) = dir 
    (i, j) = pos    
    if grid[i][j] == '#': return False
    elif grid[i][j] == '@':
        return check((i + dx, j + dy), dir)
    elif grid[i][j] == ']':
        if dir == (1, 0) or dir == (-1, 0):
            ok1 = check((i + dx, j + dy), dir)
            ok2 = check((i + dx, (j - 1) + dy), dir)
            return ok1 and ok2
        else:
            return check((i, j - 2), dir) 
    elif grid[i][j] == '[': 
        if dir == (1, 0) or dir == (-1, 0):
            ok1 = check((i + dx, j + dy), dir)
            ok2 = check((i + dx, (j + 1) + dy), dir)
            return ok1 and ok2
        else:
            return check((i, j + 2), dir) 
    return True 
        
def simulate(pos, dir):
    (dx, dy) = dir 
    (i, j) = pos    
    if grid[i][j] == '#': return
    elif grid[i][j] == '@':
        simulate((i + dx, j + dy), dir)
        grid[i][j], grid[i + dx][j + dy] = grid[i + dx][j + dy], grid[i][j]
        global robot
        robot = (i + dx, j + dy)
    elif grid[i][j] == ']':
        if dir == (1, 0) or dir == (-1, 0):
            simulate((i + dx, j + dy), dir)
            simulate((i + dx, (j - 1) + dy), dir)
            grid[i][j], grid[i + dx][j] = grid[i + dx][j], grid[i][j]
            grid[i][j - 1], grid[i + dx][j - 1] = grid[i + dx][j - 1], grid[i][j - 1]
        else:
            simulate((i, j - 2), dir) 
            grid[i][j - 1], grid[i][j - 2] = grid[i][j - 2], grid[i][j - 1]
            grid[i][j - 1], grid[i][j] = grid[i][j], grid[i][j - 1]
    elif grid[i][j] == '[': 
        if dir == (1, 0) or dir == (-1, 0):
            simulate((i + dx, j + dy), dir)
            simulate((i + dx, (j + 1) + dy), dir)
            grid[i][j], grid[i + dx][j] = grid[i + dx][j], grid[i][j]
            grid[i][j + 1], grid[i + dx][j + 1] = grid[i + dx][j + 1], grid[i][j + 1]
        else:
            simulate((i, j + 2), dir) 
            grid[i][j + 1], grid[i][j + 2] = grid[i][j + 2], grid[i][j + 1]
            grid[i][j + 1], grid[i][j] = grid[i][j], grid[i][j + 1]
    return
 
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
    if move == '^': 
        if check(robot, (-1, 0)):
            simulate(robot, (-1, 0))
    elif move == '<':
        if check(robot, (0, -1)):
            simulate(robot, (0, -1))
    elif move == '>': 
        if check(robot, (0, 1)):
            simulate(robot, (0, 1)) 
    elif move == 'v': 
        if check(robot, (1, 0)):
            simulate(robot, (1, 0))
    else: pass
ans = 0 

for i in range(n):
    for j in range(m):
        if grid[i][j] == '[': ans += 100 * i + j
print(ans)
    

