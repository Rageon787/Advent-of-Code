import sys 
from collections import defaultdict
sys.setrecursionlimit(10000000)


directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
garden = []
filename = sys.argv[1]
with open(filename) as f:
    for line in f: garden.append("#" + line.strip() + "#") 
n, m = len(garden), len(garden[0])
garden = ["#" * m] + garden + ["#" * m]
n, m = len(garden), len(garden[0])
area, perimter = 0, 0
def solve(pos):
    (x, y) = pos 
     
    if (x, y) in visited:
        return 
    visited.add((x, y)) 
    global area, perimeter
    area += 1 
    
    for (dx, dy) in directions:
        if x + dx not in range(n) or y + dy not in range(m): perimeter += 1
        elif garden[x + dx][y + dy] != garden[x][y]:
            perimeter += 1
            border[(x + dx, y + dy)].append((dx, dy))
        else: solve((x + dx, y + dy))
    
    return
 

visited = set()
ans = 0
for i in range(n):
    for j in range(m):
        if garden[i][j] != "#" and (i, j) not in visited:
            area, perimeter, sides = 0, 0, 0
            border = defaultdict(list)
            solve((i, j))

            for r in range(n):
                previous_north, previous_south = False, False
                for c in range(m): 
                    if (-1, 0) in border[(r, c)]: 
                        if not previous_north: sides += 1
                        previous_north = True
                    else: previous_north = False

                    if (1, 0) in border[(r, c)]:
                        if not previous_south: sides += 1
                        previous_south = True 
                    else: previous_south = False

            for c in range(m):
                previous_east, previous_west = False, False 
                for r in range(n):  
                    if (0, 1) in border[(r, c)]:
                        if not previous_west: sides += 1
                        previous_west = True
                    else: previous_west = False
                    if (0, -1) in border[(r, c)]:
                        if not previous_east: sides += 1
                        previous_east = True 
                    else: previous_east = False
                    
            ans += (area * sides)
print(ans)




