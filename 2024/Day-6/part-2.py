import sys 
sys.setrecursionlimit(10000000)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # up -> right -> down -> left 

grid = [] 
visited = set()
filename = sys.argv[1]
with open(filename) as f:
    for line in f:
        grid.append(list(line.strip("\n")))
ans2 = set()
def simulate(pos, direction):
    (i, j) = pos                        # Position vector 
    (x, y) = directions[direction]      # direction vector
    if (i, j, direction) in visited:
       return 
    visited.add((i, j, direction))
    grid[i][j] = 'X'

    if i + x not in range(n) or j + y not in range(m):      # The Guard is out of the grid
        return 

    if grid[i + x][j + y] == "#":                                # guard has hit an obstruction on the current direction
        simulate((i, j), (direction + 1) % 4)              # Turn 90 degrees to the right 
    else: 
        grid[i + x][j + y] = '#'
        di, dj, changed_direction = i, j, (direction + 1) % 4 
        visited2 = set()
        escaped = False
        while True:
            dx, dy = directions[changed_direction] 
            if (di, dj, changed_direction) in visited2:
                break
            visited2.add((di, dj, changed_direction))
            if di + dx not in range(n) or dj + dy not in range(m):
                escaped = True 
                break 
            elif grid[di + dx][dj + dy] == '#':
                changed_direction = (changed_direction + 1) % 4
            else:
                di += dx 
                dj += dy
        if not escaped: ans2.add((i, j))
        grid[i + x][j + y] = '.' 
        simulate((i + x, j + y), direction)                # Move in the same direction 
    return
    

    
n, m = len(grid), len(grid[0])
for i in range(n):
    for j in range(m):
        if grid[i][j] == "^": simulate((i, j), 0)
        elif grid[i][j] == ">": simulate((i, j), 1)
        elif grid[i][j] == "v": simulate((i, j), 2)
        elif grid[i][j] == "<": simulate((i, j), 3)
        else: continue

ans = 0 
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'X': ans += 1
print(len(ans2)) 
