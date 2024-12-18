import sys 

sys.setrecursionlimit(10000000)


directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
garden = []
with open("input.txt") as f:
    for line in f: garden.append(line.strip()) 
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
        elif garden[x + dx][y + dy] != garden[x][y]: perimeter += 1
        else: solve((x + dx, y + dy))
    
    return
 
visited = set()
ans = 0
for i in range(n):
    for j in range(m):
        if (i, j) not in visited:
            area, perimeter = 0, 0
            solve((i, j))
            ans += (area * perimeter)
print(ans)




