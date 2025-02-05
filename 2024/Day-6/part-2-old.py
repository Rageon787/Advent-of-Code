import sys 
sys.setrecursionlimit(10000000)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # up -> right -> down -> left 


def simulate(pos, direction):
    (i, j) = pos                        # Position vector 
    (x, y) = directions[direction]      # direction vector
    if i + x >= n or j + y >= m or i + x < 0 or j + y < 0:      # The Guard is out of the grid
        return 
    if (i, j, direction) in visited:
        return
    visited.add((i, j, direction))
        # Add an obstruction to point (i + x, j + y) and check if the guard reaches a visited cell 
    changed_direction = (direction + 1) % 4             # Change in direction after hitting the new obstruction
    ni, nj = i, j
    ok = False
    visited2 = set()
    while not ok:
        (xi, yi) = directions[changed_direction] 
        if ni + xi >= n or nj + yi >= m or ni + xi < 0 or nj + yi < 0:
            break
        if (ni, nj, changed_direction) in visited2 or (ni, nj, changed_direction) in visited:
            ok = True
            break 
        visited2.add((ni, nj, changed_direction))

        if grid[ni + xi][nj + yi] == '#':
            changed_direction += 1 
            changed_direction %= 4
        else:
            ni += xi
            nj += yi
    if ok:
        grid[i][j] = 'C' 
        
    if grid[i + x][j + y] == "#":                                # guard has hit an obstruction on the current direction
        simulate((i, j), (direction + 1) % 4)              # Turn 90 degrees to the right 
    else: 
        simulate((i + x, j + y), direction)                # Move in the same direction 
    return
    

grid = [] 
visited = set()
with open("sample.txt", "r") as f:
    for line in f:
        grid.append(list(line.strip("\n")))
   
n, m = len(grid), len(grid[0])
for i in range(n):
    for j in range(m):
        if grid[i][j] == "^": simulate((i, j), 0)
        elif grid[i][j] == ">": simulate((i, j), 1)
        elif grid[i][j] == "v": simulate((i, j), 2)
        elif grid[i][j] == "<": simulate((i, j), 3)
        else: continue


ans = 0
for g in grid: print(g)
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'C': ans += 1
print(ans)


 