import sys 
sys.setrecursionlimit(10000000)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # up -> right -> down -> left 

grid = [] 
visited = set()
ans = set()
with open("input.txt", "r") as f:
    for line in f:
        grid.append(list(line.strip("\n")))

def simulate(pos, direction):
    (i, j) = pos                        # Position vector 
    (x, y) = directions[direction]      # direction vector

    visited.add((i, j, direction))
    if i + x not in range(n) or j + y not in range(m):      # The Guard is out of the grid
        return 
    elif grid[i + x][j + y] == "#":                                # guard has hit an obstruction on the current direction
        simulate((i, j), (direction + 1) % 4)              # Turn 90 degrees to the right 
    else: 
        di, dj, changed_direction = i, j, (direction + 1) % 4
        visited2 = set()
        ok = False

        while True:
            (dx, dy) = directions[changed_direction]
            if di + dx not in range(n) or dj + dy not in range(m):
                break
            if (di, dj, changed_direction) in visited2 or (di, dj, changed_direction) in visited:
                ok = True
                break
            visited2.add((di, dj, changed_direction))
            if grid[di + dx][dj + dy] == '#':
                changed_direction = (changed_direction + 1) % 4 
                continue
            else:
                di += dx 
                dj += dy
                    
        if ok: ans.add((i, j, direction))  
        simulate((i + x, j + y), direction)                # Move in the same direction 
    return
    

    
n, m = len(grid), len(grid[0])
for i in range(n):
    for j in range(m):
        if grid[i][j] == '.' or grid[i][j] == '#': continue
        else:
            header = grid[i][j]
            grid[i][j] = '.'
            if header == "^": simulate((i, j), 0)
            elif header == ">": simulate((i, j), 1)
            elif header == "v": simulate((i, j), 2)
            elif header == "<": simulate((i, j), 3)
ans2 = 0
for a in ans:
    (i, j, direction) = a
    if grid[i][j] == '.': ans2 += 1
print(ans2) 